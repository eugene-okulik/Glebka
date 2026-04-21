import pytest
import requests

URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


@pytest.fixture
def setup_object():
    body = {
        "name": "Gleb",
        "data": {
            "year": 2026,
            "price": 100
        }
    }

    response = requests.post(URL, json=body, headers=HEADERS)

    if response.status_code != 200:
        pytest.fail(f"Не удалось создать объект. Status: {response.status_code}")

    obj_id = response.json()["id"]
    print(f"Object created: {obj_id}")

    yield obj_id

    requests.delete(f"{URL}/{obj_id}")
    print(f"Object deleted: {obj_id}")


@pytest.fixture(autouse=True)
def around_test():
    print("before test")
    yield
    print("after test")


def pytest_sessionstart(session):
    print("Start testing")


def pytest_sessionfinish(session, exitstatus):
    print("Testing completed")


@pytest.mark.parametrize("name, year, price", [
    ("Gleb1", 2026, 100),
    ("Gleb2", 2027, 200),
    ("Gleb3", 2028, 300),
])
def test_create(name, year, price):
    body = {
        "name": name,
        "data": {
            "year": year,
            "price": price
        }
    }

    response = requests.post(URL, json=body, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["name"] == name


@pytest.mark.medium
def test_put(setup_object):
    obj_id = setup_object

    body = {
        "name": "UPDATED_Gleb",
        "data": {
            "year": 2026,
            "price": 999
        }
    }

    response = requests.put(f"{URL}/{obj_id}", json=body, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["name"] == body["name"]


def test_patch(setup_object):
    obj_id = setup_object

    body = {"name": "PATCHED_Gleb"}

    response = requests.patch(f"{URL}/{obj_id}", json=body, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["name"] == body["name"]


@pytest.mark.critical
def test_get(setup_object):
    obj_id = setup_object

    response = requests.get(f"{URL}/{obj_id}")

    assert response.status_code == 200
    assert response.json()["id"] == obj_id


def test_delete(setup_object):
    obj_id = setup_object

    response = requests.delete(f"{URL}/{obj_id}")

    assert response.status_code == 200
