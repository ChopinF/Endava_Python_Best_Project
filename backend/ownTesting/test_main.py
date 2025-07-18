import pytest
import requests

# -------------------- /pow --------------------


# test_math.py
def test_add():
    assert 2 + 2 == 4


BASE_URL = "http://localhost:8000"
HEADERS = {"name": "key"}


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
    response = requests.post(
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
    response = requests.post(
        f"{BASE_URL}/pow/complex", headers=HEADERS, json={"a": a, "b": b}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
    assert isinstance(data["cached"], bool)


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
    ],
)
def test_fibo_retrieve(number, expected):
    response = requests.post(
        f"{BASE_URL}/fibo/retrieve", headers=HEADERS, json={"number": number}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
    assert isinstance(data["cached"], bool)


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ],
)
def test_fact_retrieve(number, expected):
    response = requests.post(
        f"{BASE_URL}/fact/retrieve", headers=HEADERS, json={"number": number}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == expected
    assert data["api_key"] == "key"
