import pytest
from src.helpers.http_client import SessionHttp


@pytest.fixture(scope="session")
def http_session():
    session = SessionHttp()
    yield session
    session.close()
