# test_example.py
import time
import pytest
from calculation import abc  # Importing the add and sub functions from one.py


def test_add(): 
    assert abc.add(1, 2) == 3
    assert abc.add(-1, 1) == 0
    assert abc.add(-1, -1) == -2

# @pytest.mark.skip(reason="This test is skipped unconditionally")
# def test_sub():
#     assert abc.sub(1, 2) == -1
#     assert abc.sub(-1, 1) == -2
#     assert abc.sub(-1, -1) == 0
    
# Custom marker for slow tests
@pytest.mark.slow
def test_example_slow():
    # Simulate a slow test
    import time
    time.sleep(3)
    assert True
    

def test_auto():
        assert 1 == 1
        assert 7 == 7
        
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
