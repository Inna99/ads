import pytest


pytestmark = pytest.mark.django_db


def test_add_create_method_not_allowed(client):
    response = client.get('/api/v1/ads/create/')
    assert response.status_code == 405
    # print(response.status_code)
    # print(response.json())
    assert response.json() == {'detail': 'Method "GET" not allowed.'}
