import pytest
from hello import add, divide
    
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

# bob = False

# @pytest.mark.skipif(bob, reason= "bob does not exist")
def test_divide():
    assert divide(12,3) == 4
    