import pytest
from datetime import datetime, date

pytestmark = pytest.mark.django_db


def test_ad_create_method_not_allowed(client):
    response = client.get("http://127.0.0.1:8000/api/v1/ads/create/")
    assert response.status_code == 405
    assert response.json() == {"detail": 'Method "GET" not allowed.'}


def test_ad_noting_delete(client):
    response = client.delete("http://127.0.0.1:8000/api/v1/ads/delete/1/")
    # assert response.status_code == 405
    # assert response.json() == {"detail": 'Method "GET" not allowed.'}
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not found.'}


def test_ad_create_then_delete(client):
    response = client.post(
        "http://127.0.0.1:8000/api/v1/ads/create/",
        data={'title': 'title1', 'body': 'add_body'}
    )
    assert response.status_code == 201
    assert response.json()['id'] == 1
    response = client.delete("http://127.0.0.1:8000/api/v1/ads/delete/1/")
    # assert response.status_code == 405
    # assert response.json() == {"detail": 'Method "GET" not allowed.'}
    assert response.status_code == 204
    assert response.content == b''


def test_ad_is_available(client):
    response = client.get("http://127.0.0.1:8000/api/v1/ads/")
    assert response.status_code == 200
    assert response.json() == []


def test_ad_big(client):
    response = client.post("http://127.0.0.1:8000/api/v1/ads/create/")
    # print(response.status_code)
    # print(response.json())
    assert response.status_code == 400
    assert response.json() == {'title': ['This field is required.'], 'body': ['This field is required.']}


def test_ad_big1(client):
    dt = datetime.now()
    response = client.post("http://127.0.0.1:8000/api/v1/ads/create/", data={'title': 'title1', 'body': ['add_body']})
    assert response.status_code == 201
    # assert response.json() == {
    #     'id': 1,
    #     'title': 'title1',
    #     'body': 'add_body',
    #     'actual': False,
    #     'date_created': str(dt),
    #     'last_modified': '2021-08-27'}

    # print(response.status_code)
    # print(response.json())

    # response = client.get("http://127.0.0.1:8000/api/v1/ads/")
    # assert response.status_code == 400
    # assert response.json() == []

def test_ad_unavailable(client):
    response = client.get("http://127.0.0.1:8000/api/v1/ads/empty.html")
    assert response.status_code == 404


# import pytest
# import requests
# import json
#
#
# # тест на создание пользователя и проверку успешного создания
# def test create_user():
#
#
# user = {"name": "Fred”, "age": 25, "mail":"fr @ mal.com", "password": "134513"}
#         url = "http://localhost/users/”
# r = requests.post(url, data=user)
# try:
#     r.raise_for_status()
# except requests.exceptions.HTTPError as e:
#     print('ERROR: %s' % e)
# assert r.text == "Ok"
#
#
# # тест на получение пользователя по id
# def test_get_user_by_id():
#     example_user = json.dumps({"name": "Ron”, "age": 39, "mail": "magicRon @ mal.com", "password": "123"})
#                                url = "http://localhost/users/1”
#     r = requests.get(url)
#     try:
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print('ERROR: %s' % e)
#     user = json.loads(r.data)
#     assert example_user == user





# def test_ad_delete_method(client):
#     response = client.delete("http://127.0.0.1:8000/api/v1/ads/delete/4/")
#     # assert response.status_code == 405
#     print(response.status_code)
#     print(response.json())
#     # assert response.json() == {"detail": 'Method "GET" not allowed.'}

#
# def test_ad_create_method(client):
#     payload = {"date_created": "2020-11-19", "title": "Go to School", "body": "Go Buy Goods from the market", "actual": True, "last_modified": "2020-11-21"}
#     response = client.post("api/v1/ads/create/", param=payload)
#     print(response.json())
#     # assert response.status_code == 405
#     # # print(response.status_code)
#     # # print(response.json())
#     # assert response.json() == {"detail": 'Method "GET" not allowed.'}
