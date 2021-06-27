import pytest

from py_skeleton.service import MyService


@pytest.fixture
def service():
    """
    Create and return dummy service
    """
    service = MyService("test_dummy")
    yield service
    # perform clean-up if any
