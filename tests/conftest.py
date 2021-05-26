import pytest

from src.helpers.http_client import SessionHttp
from src.configuration.config import Config


@pytest.fixture(scope="session")
def http_session():
    session = SessionHttp()
    yield session
    session.close()


@pytest.fixture(scope="session")
def config():
    config = Config().hierarchy_loader().get_configuration()
    yield config
