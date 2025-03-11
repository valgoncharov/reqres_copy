import pytest
from typing import Dict
from .conftest import assert_response_time

# Constants
BASE_URL = "https://reqres.in/api"


@pytest.fixture
def user_data() -> Dict:
    """Fixture to get user data for testing"""
    return {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }


@pytest.fixture
def create_user_data() -> Dict:
    """Fixture for user creation data"""
    return {
        "name": "morpheus",
        "job": "leader"
    }


def test_get_single_user(api_client, base_url, user_data):
    """Test getting a single user's data"""
    with assert_response_time():
        response = api_client.get(f"{base_url}/users/{user_data['id']}")

    assert response.status_code == 200
    data = response.json()['data']

    assert data['id'] == user_data['id']
    assert data['email'] == user_data['email']
    assert data['first_name'] == user_data['first_name']
    assert data['last_name'] == user_data['last_name']
    assert data['avatar'] == user_data['avatar']


def test_get_nonexistent_user(api_client, base_url):
    """Test getting a user that doesn't exist"""
    with assert_response_time():
        response = api_client.get(f"{base_url}/users/{user_data['id']}")

    assert response.status_code == 404


def test_list_users(api_client, base_url):
    """Test getting list of users"""
    with assert_response_time():
        response = api_client.get(f"{base_url}/users")

    assert response.status_code == 200
    data = response.json()

    assert 'page' in data
    assert 'per_page' in data
    assert 'total' in data
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) > 0


def test_create_user(api_client, base_url, create_user_data):
    """Test creating a new user"""
    with assert_response_time():
        response = api_client.post(f"{base_url}/users", json=create_user_data)

    assert response.status_code == 201
    data = response.json()

    assert data['name'] == create_user_data['name']
    assert data['job'] == create_user_data['job']
    assert 'id' in data
    assert 'createdAt' in data


def test_update_user(api_client, base_url, create_user_data):
    """Test updating a user"""
    updated_data = create_user_data.copy()
    updated_data['job'] = "zion resident"

    with assert_response_time():
        response = api_client.put(
            f"{base_url}/users/{user_data['id']}", json=updated_data)

    assert response.status_code == 200
    data = response.json()

    assert data['name'] == updated_data['name']
    assert data['job'] == updated_data['job']
    assert 'updatedAt' in data


def test_delete_user(api_client, base_url):
    """Test deleting a user"""
    with assert_response_time():
        response = api_client.delete(f"{base_url}/users/{user_data['id']}")

    assert response.status_code == 204


@pytest.mark.parametrize("page,expected_status", [
    (1, 200),
    (2, 200),
    (999, 200),  # Empty page but still valid
])
def test_user_pagination(api_client, base_url, page, expected_status):
    """Test user listing pagination"""
    with assert_response_time():
        response = api_client.get(f"{base_url}/users", params={"page": page})

    assert response.status_code == expected_status
    data = response.json()

    assert 'page' in data
    assert data['page'] == page
