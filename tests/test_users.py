from utils.api_client import get, post, put, delete

def test_get_single_user_by_id():
    response = get("/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    assert data["data"]["first_name"] is not None
    assert data["data"]["last_name"] is not None
    assert response.elapsed.total_seconds() < 0.5

def test_create_user():
    payload = {
        "name": "Flower",
        "job": "QA Engineer"
    }
    response = post("/users", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data
    assert "createdAt" in data
    assert response.elapsed.total_seconds() < 0.5

def test_update_user():
    payload = {
        "name": "Flower",
        "job": "Senior QA Engineer"
    }
    response = put("/users/2", payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data
    assert response.elapsed.total_seconds() < 0.5

def test_delete_user():
    response = delete("/users/2")
    assert response.status_code == 204
    assert response.text == "" or response.text is not None
    assert response.elapsed.total_seconds() < 0.5