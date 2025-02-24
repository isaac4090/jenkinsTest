from funcitons import bob
import pytest 


def test_add():
    Bob = bob()
    assert Bob.addNumbers(3,4) == 7

def test_list():
    Bob = bob()
    intialSize = len(Bob.list)

    Bob.addToList("hello")
    newSize = len(Bob.list)

    assert newSize == intialSize +1