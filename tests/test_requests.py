import requests
import json
from tests.data.create_user import CreateUser
from tests.data.create_user_response import CreateUserResponse
from utils.file_reader import read_file
from tests.base_test import set_up


def test_get_users(set_up):
    response = requests.get(set_up['base_uri'] + 'users?page=2', headers=set_up['headers'])
    assert response.status_code == 200

    data = json.loads(response.text)
    assert data['page'] == 2


def test_get_user_not_found(set_up):
    response = requests.get(set_up['base_uri'] + 'users/100', headers=set_up['headers'])
    assert response.status_code == 404


def test_delete_request(set_up):
    response = requests.delete(set_up['base_uri'] + 'users/2', headers=set_up['headers'])
    assert response.status_code == 204


def test_post_request(set_up):
    body = read_file('data.json')

    response = requests.post(set_up['base_uri'] + 'users', json=body['user_data'][0], headers=set_up['headers'])
    assert response.status_code == 201

    data = json.loads(response.text)

    assert data['name'] == body['user_data'][0]['name']
    assert data['job'] == body['user_data'][0]['job']


def test_put_request(set_up):
    body = read_file('data.json')

    response = requests.put(set_up['base_uri'] + 'users/2', json=body['user_data'][1], headers=set_up['headers'])
    assert response.status_code == 200

    data = json.loads(response.text)

    assert data['name'] == body['user_data'][1]['name']
    assert data['job'] == body['user_data'][1]['job']


def test_patch_request(set_up):
    body = read_file('data.json')

    response = requests.patch(set_up['base_uri'] + 'users/2', json=body['user_data'][2], headers=set_up['headers'])
    assert response.status_code == 200

    data = json.loads(response.text)

    assert data['job'] == body['user_data'][2]['job']


def test_post_login_successful(set_up):
    body = read_file('data.json')
    print(body['login_data'][0])
    response = requests.post(set_up['base_uri'] + 'login', json=body['login_data'][0], headers=set_up['headers'])
    assert response.status_code == 200

    data = json.loads(response.text)
    assert data['token'] == 'QpwL5tke4Pnpja7X4'


def test_post_login_unsuccessful(set_up):
    body = read_file('data.json')

    response = requests.post(set_up['base_uri'] + 'login', json=body['login_data'][1], headers=set_up['headers'])
    assert response.status_code == 400

    data = json.loads(response.text)
    assert data['error'] == "Missing password"


def test_post_register_successful(set_up):
    user = CreateUser()
    user.set_email('eve.holt@reqres.in')
    user.set_password('pistol')

    # converts the object to json
    user_json = json.dumps(user.__dict__)
    # json.loads converts the json to a dictionary
    response = requests.post(set_up['base_uri'] + 'register', json=json.loads(user_json), headers=set_up['headers'])
    assert response.status_code == 200
    # get the response body as a dictionary
    data = json.loads(response.text)
    # create a new object from the dictionary
    user_response = CreateUserResponse(**data)

    assert user_response.get_id() == 4
    assert user_response is not None
