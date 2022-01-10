import pytest


@pytest.fixture
def set_up():
    base_uri = 'https://reqres.in/api/'
    headers = {'Content-Type': 'application/json'}
    return {'base_uri': base_uri, 'headers': headers}
