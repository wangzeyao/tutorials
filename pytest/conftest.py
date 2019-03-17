import pytest


@pytest.fixture(scope='session')
def count():
    print('init count')
    return 10