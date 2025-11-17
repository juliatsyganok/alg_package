import sys
import pytest 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fact_fib import factorial, factorial_recursive, fibo, fibo_recursive

def test_factorial_positive_numbers():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_negative_should_raise_error():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_recursive_positive_numbers():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(7) == 5040

def test_factorial_recursive_negative_should_raise_error():
    with pytest.raises(ValueError):
        factorial_recursive(-1)

def test_fib_positive_numbers():
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(5) == 5
    assert fibo(10) == 55

def test_fib_negative_should_raise_error():
    with pytest.raises(ValueError):
        fibo(-1)

def test_fib_recursive_positive_numbers():
    assert fibo_recursive(0) == 0
    assert fibo_recursive(1) == 1
    assert fibo_recursive(5) == 5
    assert fibo_recursive(10) == 55
