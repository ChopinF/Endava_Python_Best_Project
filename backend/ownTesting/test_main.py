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
