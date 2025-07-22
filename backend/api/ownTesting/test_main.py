import pytest
from fastapi.testclient import TestClient
from ..main import app


## simple test for pytest
def test_add():
    assert 2 + 2 == 4


BASE_URL = "http://localhost:8000"
HEADERS = {"name": "key"}
client = TestClient(app)


# -------------------- /pow --------------------
def simple_test():
    pass


def test_pow_float_simple():
    with TestClient(app) as client:
        payload = {"a": 2, "b": 2}
        response = client.post(f"{BASE_URL}/pow/float", json=payload, headers=HEADERS)
        assert response.status_code == 200


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, -1, 0.5),
        (4, 0.5, 2.0),
        (5, 2, 25.0),
    ],
)
def test_pow_float(a, b, expected):
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/pow/float", headers=HEADERS, json={"a": a, "b": b}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == expected
        assert data["api_key"] == "key"
        assert isinstance(data["cached"], bool)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 1, 2),
        (4, 3, 64),
        (5, 3, 125),
    ],
)
def test_pow_int(a, b, expected):
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/pow/int", headers=HEADERS, json={"a": a, "b": b}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == expected
        assert data["api_key"] == "key"
        assert isinstance(data["cached"], bool)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("1+1j", "2", "2j"),
        ("2+0j", "2", "4+0j"),
        ("0+1j", "2", "-1+0j"),
    ],
)
def test_pow_complex(a, b, expected):
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/pow/complex", headers=HEADERS, json={"a": a, "b": b}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == expected
        assert data["api_key"] == "key"
        assert isinstance(data["cached"], bool)


def test_pow_root():
    with TestClient(app) as client:
        response = client.get(f"{BASE_URL}/pow/")
        assert response.status_code == 200
        assert "int" in response.json()


def test_pow_delete_cache():
    with TestClient(app) as client:
        response = client.delete(
            f"{BASE_URL}/pow/",
            headers=HEADERS,
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
@pytest.mark.parametrize("operand_type, payload, expected", [
    ("int", {"a": 2, "b": 3}, 8),
    ("float", {"a": 4.0, "b": 0.5}, 2.0),
    ("complex", {"a": "1+1j", "b": "2"}, 2j),
])


def test_pow_types_compute_and_cache(operand_type, payload, expected):
    with TestClient(app) as client:
        # First call should compute and store in cache
        response = client.post(
            f"{BASE_URL}/pow/{operand_type}",
            headers=HEADERS,
            json=payload
        )
        assert response.status_code == 200
        result = response.json()
        if operand_type == "complex":
            assert complex(result["answer"]) == expected
        else:
            assert result["answer"] == expected
        assert result["cached"] is False
        assert result["api_key"] == "key"

        # Second call should fetch from cache
        response_cached = client.post(
            f"{BASE_URL}/pow/{operand_type}",
            headers=HEADERS,
            json=payload
        )
        assert response_cached.status_code == 200
        result_cached = response_cached.json()
        if operand_type == "complex":
            assert complex(result["answer"]) == expected
        else:
            assert result["answer"] == expected
        assert result_cached["cached"] is True


def test_pow_invalid_operand_type():
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/pow/unknown",
            headers=HEADERS,
            json={"a": 2, "b": 3}
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Unsupported operand type"


def test_pow_bad_payload_causes_exception():
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/pow/int",
            headers=HEADERS,
            json={"a": "bad", "b": 2}
        )
        assert response.status_code == 422
        data = response.json()
        assert isinstance(data, dict)
        assert "detail" in data
        assert any("input" in str(item) for item in data["detail"])

# # -------------------- /fibo --------------------
@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
    ],
)
def test_fibo_retrieve(number, expected):
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/fibo/retrieve", headers=HEADERS, json={"number": number}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == expected
        assert data["api_key"] == "key"
        assert isinstance(data["cached"], bool)


def test_fibo_root():
    with TestClient(app) as client:
        response = client.get(f"{BASE_URL}/fibo/")
        assert response.status_code == 200
        assert response.text.strip('"') == "good fibo"


def test_fibo_delete_cache():
    with TestClient(app) as client:
        response = client.delete(f"{BASE_URL}/fibo/", headers=HEADERS)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
@pytest.mark.parametrize("n, expected_sequence", [
    (9, [1, 2, 3, 5, 8, 13, 21, 34]),  # caches fibo(1) to fibo(8)
])
def test_fibo_populate(n, expected_sequence):
    with TestClient(app) as client:
        # Trigger population (caches up to fibo(n-1))
        response = client.post(
            f"{BASE_URL}/fibo/",
            headers=HEADERS,
            json={"number": n}
        )
        assert response.status_code == 200

        # Validate fibo(1) to fibo(n-1) are cached
        for i, expected in enumerate(expected_sequence, start=1):
            retrieve = client.post(
                f"{BASE_URL}/fibo/retrieve",
                headers=HEADERS,
                json={"number": i}
            )
            assert retrieve.status_code == 200
            result = retrieve.json()
            assert result["answer"] == expected, f"fibo({i}) mismatch"
            assert result["cached"] is True

        # Additionally test fibo(n) exists but is not cached
        final = client.post(
            f"{BASE_URL}/fibo/retrieve",
            headers=HEADERS,
            json={"number": n}
        )
        assert final.status_code == 200
        result = final.json()
        assert result["answer"] == 55, "fibo(n) value mismatch"
        assert result["cached"] is False  # ✅ not cached due to populate logic


# -------------------- /fact --------------------
def test_fact_root():
    with TestClient(app) as client:
        response = client.get(
            f"{BASE_URL}/fact/",
        )
        assert response.status_code == 200
        assert response.text.strip('"') == "good fact"


def test_fact_delete_cache():
    with TestClient(app) as client:
        response = client.delete(f"{BASE_URL}/fact/", headers=HEADERS)
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ],
)
def test_fact_retrieve(number, expected):
    with TestClient(app) as client:
        client.delete(f"{BASE_URL}/fact/", headers=HEADERS)

        response = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": number},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == expected
        assert data["api_key"] == "key"
        assert data["cached"] is False

        response_cached = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": number},
        )
        assert response_cached.status_code == 200
        data_cached = response_cached.json()
        assert data_cached["answer"] == expected
        assert data_cached["cached"] is True

def test_fact_populate_basic():
    with TestClient(app) as client:
        # Clear cache before populating
        client.delete(f"{BASE_URL}/fact/", headers=HEADERS)

        # Populate up to 5
        response = client.post(
            f"{BASE_URL}/fact/",
            headers=HEADERS,
            json={"number": 5},
        )
        # The endpoint does not return anything, so status should be 204 or 200
        assert response.status_code in (200, 204)

        # Now retrieve factorial of 5, should be cached
        response_retrieve = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": 5},
        )
        assert response_retrieve.status_code == 200
        data = response_retrieve.json()
        assert data["answer"] == 120
        assert data["cached"] is True
        assert data["api_key"] == "key"

def test_fact_populate_zero():
    with TestClient(app) as client:
        client.delete(f"{BASE_URL}/fact/", headers=HEADERS)
        response = client.post(
            f"{BASE_URL}/fact/",
            headers=HEADERS,
            json={"number": 0},
        )
        assert response.status_code in (200, 204)
        # First retrieval: not cached
        response_retrieve = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": 0},
        )
        assert response_retrieve.status_code == 200
        data = response_retrieve.json()
        assert data["answer"] == 1
        assert data["cached"] is False

        # Second retrieval: should be cached
        response_retrieve_2 = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": 0},
        )
        assert response_retrieve_2.status_code == 200
        data2 = response_retrieve_2.json()
        assert data2["answer"] == 1
        assert data2["cached"] is True

def test_fact_populate_large():
    with TestClient(app) as client:
        client.delete(f"{BASE_URL}/fact/", headers=HEADERS)
        # Populate up to a large number (e.g., 10)
        response = client.post(
            f"{BASE_URL}/fact/",
            headers=HEADERS,
            json={"number": 10},
        )
        assert response.status_code in (200, 204)
        # Retrieve factorial of 10, should be cached
        response_retrieve = client.post(
            f"{BASE_URL}/fact/retrieve",
            headers=HEADERS,
            json={"number": 10},
        )
        assert response_retrieve.status_code == 200
        data = response_retrieve.json()
        assert data["answer"] == 3628800
        assert data["cached"] is True

def test_fact_populate_missing_auth():
    with TestClient(app) as client:
        # Try to populate without API key
        response = client.post(
            f"{BASE_URL}/fact/",
            json={"number": 5},
        )
        assert response.status_code == 403
        
def test_invalid_api_key_rejected():
    with TestClient(app) as client:
        response = client.post(
            f"{BASE_URL}/fibo/retrieve",  # or any protected route
            headers={"name": "WRONG_KEY"},  # 🔥 intentionally incorrect
            json={"number": 5}
        )
        assert response.status_code == 403
        assert response.json() == {"detail": "Could not validate API KEY"}
