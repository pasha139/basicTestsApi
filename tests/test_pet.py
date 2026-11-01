import pytest
import json


def test_response_on_base_url(api_session):
    response = api_session.get(api_session.base_url)
    assert response.status_code == 404 # response on base url 404 this is right btw


def test_pet_create(api_session, base_Pet):
    response = api_session.post(f"{api_session.base_url}/pet", json=base_Pet)
    body = response.json()
    assert response.status_code == 200
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_put(api_session, base_Pet):
    response = api_session.put(f"{api_session.base_url}/pet", json=base_Pet)
    body = response.json()
    assert response.status_code == 200
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_get_findByStatus(api_session, base_Pet):
    response = api_session.get(f"{api_session.base_url}/pet/findByStatus", params={'status': 'available'})
    body = response.json()
    assert response.status_code == 200
    assert all(pet['status'] == 'available' for pet in body)


def test_pet_findPetByID(api_session, base_Pet):
    response = api_session.get(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    body = response.json()
    assert response.status_code == 200
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_updateById(api_session, base_Pet, update_Pet):
    response = api_session.post(
        f"{api_session.base_url}/pet/{base_Pet['id']}", 
        data={'name': update_Pet['name'], 'status': update_Pet['status']}
    ) 
    body = response.json()
    assert response.status_code == 200
    assert body['code'] == 200

    response = api_session.get(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    body = response.json()
    assert response.status_code == 200 
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        if field in ("name", "status"):
            assert body[field] == update_Pet[field] 
            continue
        assert body[field] == base_Pet[field] 






