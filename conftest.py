import pytest 
import requests
from models.pet import Pet, Category, Tag
from models.user import User


@pytest.fixture
def base_Pet() -> Pet:
    return Pet(
        id=12345,
        name="Buddy",
        photoUrls=["https://example.com/photos/buddy1.jpg"],
        category=Category(id=1, name="Dogs"),
        tags=[Tag(id=10, name="friendly")],
        status="available",
    )


@pytest.fixture
def base_User() -> User:
    return User(
        id=100,
        username="base",
        firstName="John",
        lastName="Doe",
        email="exp@gmail.com",
        password="Pass",
        phone="1234567",
        userStatus=100,
    )


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.base_url = "https://petstore.swagger.io/v2"
    yield session
    session.close()

