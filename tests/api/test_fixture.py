import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Igor'

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Orlov'

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''