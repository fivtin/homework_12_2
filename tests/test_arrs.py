import pytest
from utils import arrs


@pytest.fixture
def test_coll():
    return [1, 2, 3]


def test_get(test_coll):
    assert arrs.get(test_coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(test_coll):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(test_coll, 1) == [2, 3]
    assert arrs.my_slice(test_coll) == [1, 2, 3]
    assert arrs.my_slice([], 10, 100) == []
