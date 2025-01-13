from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_2():
    response = client.get("/prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_3():
    response = client.get("/prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_4():
    response = client.get("/prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_1():
    response = client.get("/prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

def test_check_prime_0():
    response = client.get("/prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_negative():
    response = client.get("/prime/-5")
    assert response.status_code == 200
    assert response.json() == {"number": -5, "is_prime": False}

def test_check_prime_large_prime():
    response = client.get("/prime/29")
    assert response.status_code == 200
    assert response.json() == {"number": 29, "is_prime": True}

def test_check_prime_large_non_prime():
    response = client.get("/prime/30")
    assert response.status_code == 200
    assert response.json() == {"number": 30, "is_prime": False}

def test_check_prime_large_number():
    response = client.get("/prime/9973")
    assert response.status_code == 200
    assert response.json() == {"number": 9973, "is_prime": True}

