import pytest


def test_response_on_base_url(api_session):
    response = api_session.get(api_session.base_url)
    assert response.status_code == 404 # response on base url 404 this is right btw


def test_pet_create(api_session, base_Pet):
    response = api_session.post(f"{api_session.base_url}/pet", json=base_Pet)
    assert response.status_code == 200
    body = response.json()
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_put(api_session, base_Pet):
    response = api_session.put(f"{api_session.base_url}/pet", json=base_Pet)
    assert response.status_code == 200
    body = response.json()
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_get_findByStatus(api_session, base_Pet):
    response = api_session.get(f"{api_session.base_url}/pet/findByStatus", params={'status': 'available'})
    assert response.status_code == 200
    body = response.json()
    assert all(pet['status'] == 'available' for pet in body)


def test_pet_findPetByID(api_session, base_Pet):
    response = api_session.get(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    assert response.status_code == 200
    body = response.json()
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        assert body[field] == base_Pet[field]


def test_pet_updateById(api_session, base_Pet, update_Pet):
    response = api_session.post(
        f"{api_session.base_url}/pet/{base_Pet['id']}", 
        data={'name': update_Pet['name'], 'status': update_Pet['status']}
    ) 
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200

    response = api_session.get(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    body = response.json()
    assert response.status_code == 200 
    for field in ("id", "name", "status", "photoUrls", "tags", "category"):
        if field in ("name", "status"):
            assert body[field] == update_Pet[field] 
            continue
        assert body[field] == base_Pet[field]


def test_pet_deleteByID(api_session, base_Pet):
    response = api_session.delete(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert int(body['message']) == base_Pet['id']

    response = api_session.get(f"{api_session.base_url}/pet/{base_Pet['id']}") 
    assert response.status_code == 404
    body = response.json()
    assert body['code'] == 1
    assert body['message'] == 'Pet not found'


def test_pet_uploadImage(api_session, base_Pet):
    with open("test_photo.jpg", "rb") as f:
        response = api_session.post(
            f"{api_session.base_url}/pet/{base_Pet['id']}/uploadImage",
            data={'additionalMetadata': 'test'},
            files={'file': ('test_photo.jpg', f, 'image/jpeg')},
            )
    assert response.status_code == 200    
    
    body = response.json()
    assert body['code'] == 200
    assert "File uploaded" in body['message']


def test_get_non_existent_pet(api_session):
    assert api_session.delete(f"{api_session.base_url}/pet/999999999").status_code in (200, 404)
    response = api_session.get(f"{api_session.base_url}/pet/999999999")
    assert response.status_code == 404


def test_create_pet_without_required_fields(api_session):
    response = api_session.post(f"{api_session.base_url}/pet", json={"status": "available"})
    assert response.status_code in (400, 405) 


def test_login_with_empty_credentials(api_session):
    response = api_session.get(f"{api_session.base_url}/user/login", params={"username": ""})
    assert response.status_code == 400
