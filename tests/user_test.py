import requests
import pytest


def test_user_data():
    url = "https://reqres.in/api/users/2"
    id = 2
    email = "janet.weaver@reqres.in"

    response = requests.get(url)
    body = response.json()
    data = body['data']

    assert data['id'] == id
    assert data['email'] == "janet.weaver@reqres.in"

