import pytest


@pytest.mark.check
def test_name(user):
    assert user.name == "Igor"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Orlov"
