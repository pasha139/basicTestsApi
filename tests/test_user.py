import pytest
import requests

def test_create_user(api_session, base_User):
    response = api_session.post(f"{api_session.base_url}/user", json=base_User)
    assert response.status_code == 200

    body = response.json()
    assert body["code"] == 200
    assert body["message"] == str(base_User['id'])
    assert body["type"] == "unknown"
    #for field in ("id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"):
    #    assert body[field] == base_User[field]


def test_create_list_with_array(api_session, base_User):
    response = api_session.post(f"{api_session.base_url}/user/createWithArray", json=[base_User])
    assert response.status_code == 200

    body = response.json()
    assert body["code"] == 200
    assert body["message"] == 'ok'
    assert body["type"] == "unknown"

    response = api_session.get(f"{api_session.base_url}/user/{base_User['username']}")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"):
        assert body[field] == base_User[field]


def test_user_login(api_session, base_User):
    response = api_session.get(
        f"{api_session.base_url}/user/login", 
        params={"username": "adm", "password": "adm"}
        )
    assert response.status_code == 200
    
    body = response.json()
    assert body['code'] == 200
    assert body['type'] == "unknown"
    assert "logged in user session:" in body['message'] 

    assert "X-Expires-After" in response.headers
    assert "X-Rate-Limit" in response.headers


def test_logout_user(api_session):
    response = api_session.get(f"{api_session.base_url}/user/logout")
    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['type'] == "unknown"
    assert body['message'] == 'ok'


def test_delete_user_by_name(api_session, base_User):
    response = api_session.delete(f"{api_session.base_url}/user/{base_User['username']}")
    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert  body['message'] == base_User['username']
    assert body['type'] == 'unknown'

    response = api_session.get(f"{api_session.base_url}/user/{base_User['username']}")
    assert response.status_code == 404

    body = response.json()
    assert body['code'] == 1
    assert  body['message'] == "User not found"
    assert body['type'] == 'error'


def test_update_user_by_name(api_session, base_User, update_User):
    response = api_session.put(
        f"{api_session.base_url}/user/{base_User['username']}",
        json=update_User
        )
    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert  body['message'] == str(update_User['id'])
    assert body['type'] == 'unknown'

    response = api_session.get(f"{api_session.base_url}/user/{update_User['username']}")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"):
        assert body[field] == update_User[field]
    

def test_find_by_name(api_session, base_User):
    response = api_session.get(f"{api_session.base_url}/user/{base_User['username']}")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"):
        assert body[field] == base_User[field]


def test_сreate_list_users(api_session, base_User):
    response = api_session.post(f"{api_session.base_url}/user/createWithList", json=[base_User])
    assert response.status_code == 200

    body = response.json()
    assert body["code"] == 200
    assert body["message"] == 'ok'
    assert body["type"] == "unknown"

    response = api_session.get(f"{api_session.base_url}/user/{base_User['username']}")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"):
        assert body[field] == base_User[field]
