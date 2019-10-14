import pytest
from framework.services.booker_client import BookerClient

booker_client = BookerClient()


@pytest.fixture()
def clear_env():
    pass
