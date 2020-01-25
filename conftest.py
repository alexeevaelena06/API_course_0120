import pytest
from api.client import BugRedClient


@pytest.fixture(scope="session")
def client():
    client = BugRedClient("http://users.bugred.ru")
    client.authorize("manager@mail.ru", "1")
    return client


def pytest_make_parametrize_id(val):
    return repr(val)