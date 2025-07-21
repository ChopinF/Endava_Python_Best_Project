import pytest
import requests
from fastapi import HTTPException
from api.endpoints.util import verify_api_key, API_KEY

# -------------------- /pow --------------------
def test_add():
    assert 2 + 2 == 4


BASE_URL = "http://localhost:8000"
HEADERS = {"name": "key"}

# -------------------- /pow --------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, -1, 0.5),
        (4, 0.5, 2.0),
        (5, 2, 25.0),
    ],
)
def test_pow_float(a, b, expected):
    response = requests.post(
        f"{BASE_URL}/pow/float", headers=HEADERS, json={"a": a, "b": b}, timeout=5
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
    response = requests.post(
        f"{BASE_URL}/pow/int", headers=HEADERS, json={"a": a, "b": b}, timeout=5
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
    response = requests.post(
        f"{BASE_URL}/pow/complex", headers=HEADERS, json={"a": a, "b": b}, timeout=5
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
    assert isinstance(data["cached"], bool)


def test_pow_root():
    response = requests.get(f"{BASE_URL}/pow/", timeout=5)
    assert response.status_code == 200
    assert "int" in response.json()


def test_pow_delete_cache():
    response = requests.delete(f"{BASE_URL}/pow/", headers=HEADERS, timeout=5)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
# -------------------- /fibo --------------------
@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
    ],
)
def test_fibo_retrieve(number, expected):
    response = requests.post(
        f"{BASE_URL}/fibo/retrieve", headers=HEADERS, json={"number": number}, timeout=5
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
    assert isinstance(data["cached"], bool)


# @pytest.mark.parametrize(
#     "number, expected",
#     [
#         (1, 1),
#         (2, 2),
#         (3, 6),
#         (4, 24),
#         (5, 120),
#         (6, 720),
#     ],
# )
def test_fibo_root():
    response = requests.get(f"{BASE_URL}/fibo/", timeout=5)
    assert response.status_code == 200
    assert response.text.strip('"') == "good fibo"


def test_fibo_delete_cache():
    response = requests.delete(f"{BASE_URL}/fibo/", headers=HEADERS, timeout=5)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# -------------------- /fact --------------------
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
    # Clear cache before testing this number
    requests.delete(f"{BASE_URL}/fact/", headers=HEADERS, timeout=5)

    # First call (should not be cached)
    response = requests.post(
        f"{BASE_URL}/fact/retrieve", headers=HEADERS, json={"number": number}, timeout=5
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
    assert data["cached"] is False

    # Cached call (should be cached)
    response_cached = requests.post(
        f"{BASE_URL}/fact/retrieve", headers=HEADERS, json={"number": number}, timeout=5
    )
    assert response_cached.status_code == 200
    data_cached = response_cached.json()
    assert data_cached["answer"] == expected
    assert data_cached["cached"] is True


def test_fact_root():
    response = requests.get(f"{BASE_URL}/fact/", timeout=5)
    assert response.status_code == 200
    assert response.text.strip('"') == "good fact"


def test_fact_delete_cache():
    response = requests.delete(f"{BASE_URL}/fact/", headers=HEADERS, timeout=5)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_verify_api_key_valid():
    result = await verify_api_key(API_KEY)
    assert result == API_KEY

@pytest.mark.asyncio
async def test_verify_api_key_invalid():
    with pytest.raises(HTTPException) as exc_info:
        await verify_api_key("wrong_key")
    assert exc_info.value.status_code == 403
    assert "Could not validate API KEY" in exc_info.value.detail