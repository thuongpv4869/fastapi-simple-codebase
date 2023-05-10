from app.config import settings

api_v1_prefix = settings.API_V1_STR


def test_read_customer(client, customer_db):
    route = f"{api_v1_prefix}/customers/{customer_db.id}"
    response = client.get(route)
    assert response.status_code == 200
    assert response.json()["id"] == customer_db.id
