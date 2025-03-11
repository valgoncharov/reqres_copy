import pytest
import requests
from typing import Dict, Generator
from contextlib import contextmanager

# Configuration
BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def api_client():
    """Session-wide test client"""
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def base_url() -> str:
    """Get the base URL for the API"""
    return BASE_URL


@contextmanager
def assert_response_time(max_duration: float = 1.0) -> Generator:
    """Context manager to assert response time is within acceptable range"""
    import time
    start_time = time.time()
    yield
    duration = time.time() - start_time
    assert duration < max_duration, f"Response took {duration:.2f}s, which is more than {max_duration}s"
