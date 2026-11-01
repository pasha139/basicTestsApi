import pytest 
import requests
from models.pet import Pet, Category, Tag
from models.user import User


@pytest.fixture
def base_Pet(api_session):
    payload = Pet(
        id=12345,
        name="Buddy",
        photoUrls=["https://example.com/photos/buddy1.jpg"],
        category=Category(id=1, name="Dogs"),
        tags=[Tag(id=10, name="friendly")],
        status="available",
    ).model_dump(exclude_none=True)
    response = api_session.post(f"{api_session.base_url}/pet", json=payload)
    assert response.status_code == 200
    yield payload
    api_session.delete(f"{api_session.base_url}/pet/{payload['id']}")


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
def base_User():
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
    yield payload


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.base_url = "https://petstore.swagger.io/v2"
    yield session
    session.close()

