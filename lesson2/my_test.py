import pytest

import main


@pytest.mark.skip(reason='not important')
def test_add():
    assert main.isFirst(3) == [1, 3]


# @pytest.mark.parametrize('list1', [5, 3, 8, 1, 2])
# def test_wrong_add(list1):
#    assert main.sort(list1)


@pytest.mark.skip(reason='dont want to see')
def test_wrong_string():
    assert main.func("hello") == "hello"


@pytest.mark.very
def test_is_0():
    assert main.isFirst(5) == [5, 7, 8]
