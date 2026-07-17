import pytest
from _pytest._code import ExceptionInfo
from .code import Code

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# -------------------
# Unit Tests
# -------------------

def test_add_two_number():
    result = add(10, 5)
    assert result == 15

def test_sub_two_number():
    result = sub(10, 5)
    assert result == 5

def test_multi_two_number():
    result = multi(10, 5)
    assert result == 50

def test_divide_two_number():
    result = divide(10, 5)
    assert result == 2.0

def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
