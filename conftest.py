import pytest 
import requests
import json
from models.pet import Pet, Category, Tag
from models.user import User
from models.order import Order


@pytest.fixture
def base_Pet(api_session):
    payload = Pet(
        id=12345,
        name="Buddy",
        photoUrls=["https://example.com/photos/buddy1.jpg"],
        category=Category(id=1, name="Dogs"),
        tags=[Tag(id=10, name="friendly")],
        status="available",
    ).model_dump(exclude_none=True, mode="json")

    response = api_session.post(f"{api_session.base_url}/pet", json=payload)
    assert response.status_code == 200
    yield payload
    response = api_session.delete(f"{api_session.base_url}/pet/{payload['id']}")
    assert response.status_code in (200, 404)
    


@pytest.fixture
def update_Pet():
    payload = Pet(
        id=6666,
        name="Rester",
        photoUrls=["https://example.com/photos/rester1.jpg"],
        category=Category(id=4, name="Cat"),
        tags=[Tag(id=8, name="Angry")],
        status="sold",
    ).model_dump(exclude_none=True)
    yield payload


@pytest.fixture
def base_User(api_session):
    payload = User(
        id=100,
        username="base",
        firstName="John",
        lastName="Doe",
        email="exp@gmail.com",
        password="Pass",
        phone="1234567",
        userStatus=100,
    ).model_dump(exclude_none=True)

    response = api_session.post(f"{api_session.base_url}/user", json=payload)
    assert response.status_code == 200
    yield payload
    response = api_session.delete(f"{api_session.base_url}/user/{payload['id']}")
    assert response.status_code in (200, 404)
    

@pytest.fixture
def update_User(api_session):
    payload = User(
        id=909,
        username="uids",
        firstName="Take",
        lastName="Pop",
        email="sos@gmail.com",
        password="Pofds",
        phone="15498093567",
        userStatus=323,
    ).model_dump(exclude_none=True)

    response = api_session.post(f"{api_session.base_url}/user", json=payload)
    assert response.status_code == 200
    yield payload
    response = api_session.delete(f"{api_session.base_url}/user/{payload['id']}")
    assert response.status_code in (200, 404)


@pytest.fixture
def base_Order(api_session):
    payload = Order(
        id=777,
        petId=111,
        quantity=333,
        shipDate="2026-11-06T11:48:21.057Z",
        status="placed",
        complete=False,
    ).model_dump(exclude_none=True, mode="json")

    response = api_session.post(f"{api_session.base_url}/store/order", json=payload)
    assert response.status_code == 200
    yield payload
    response = api_session.delete(f"{api_session.base_url}/store/order/{payload["id"]}")
    assert response.status_code in (200, 404)


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.base_url = "https://petstore.swagger.io/v2"
    yield session
    session.close()

