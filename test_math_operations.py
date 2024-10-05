# test_math_operations.py

import pytest
from math_operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 6 #5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(0, 1) == -1

def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, -2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
