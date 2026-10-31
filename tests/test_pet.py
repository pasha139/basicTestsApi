import pytest


def test_reponese_on_base_url(api_session):
    response = api_session.get(api_session.base_url)
    assert response.status_code == 404 # response on base url 404 this is right btw




