import pytest
import json


def test_reponese_on_base_url(api_session):
    response = api_session.get(api_session.base_url)
    assert response.status_code == 404 # response on base url 404 this is right btw


def test_pet_create(api_session, base_Pet):
    response = api_session.post(f"{api_session.base_url}/pet", json=base_Pet)
    body = response.json()
    assert response.status_code == 200
    for field in ("id", "name", "status", "photoUrls", "tags", "status", "category"):
        assert body[field] == base_Pet[field]



