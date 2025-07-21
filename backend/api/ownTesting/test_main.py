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
