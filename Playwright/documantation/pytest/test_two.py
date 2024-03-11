import pytest

@pytest.mark.important_test
def test_one():
    assert (1, 2, 3) == (1, 3, 3)