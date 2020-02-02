import pytest
from api.client import BugRedClient


@pytest.fixture(scope="session")
def client(email="manager@mail.ru", password='1'):
    client = BugRedClient("http://users.bugred.ru")
    client.authorize(email, password)
    return client


def pytest_make_parametrize_id(val):
    return repr(val)