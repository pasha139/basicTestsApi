import pytest
from datetime import timezone, datetime


def test_inventory(api_session):
    response = api_session.get(f"{api_session.base_url}/store/inventory", json={"additionalProp1": 12})
    assert response.status_code == 200


def test_create_order(api_session, base_Order):
    response = api_session.post(f"{api_session.base_url}/store/order", json=base_Order)
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "petId", "quantity", "shipDate", "status", "complete"):
        if field == "shipDate":
            assert datetime.fromisoformat(body[field]) == datetime.fromisoformat(base_Order[field])
            continue
        assert body[field] == base_Order[field]
        

def test_find_order_by_ID(api_session, base_Order):
    response = api_session.get(f"{api_session.base_url}/store/order/{base_Order["id"]}")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "petId", "quantity", "shipDate", "status", "complete"):
        if field == "shipDate":
            assert datetime.fromisoformat(body[field]) == datetime.fromisoformat(base_Order[field])
            continue
        assert body[field] == base_Order[field]


def test_delete_order_by_ID(api_session, base_Order):
    response = api_session.delete(f"{api_session.base_url}/store/order/{base_Order["id"]}")
    assert response.status_code == 200

    body = response.json()
    assert body["code"] == 200
    assert body["message"] == str(base_Order["id"])
    assert body["type"] == "unknown"


    
        
    
        
    
    