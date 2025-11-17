import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from stack import Stack

def test_stack_initialization():
    stack = Stack()
    assert len(stack) == 0
    assert stack.is_empty() == True

def test_stack_push_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    assert len(stack) == 3
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert len(stack) == 0

def test_stack_peek():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    
    assert stack.peek() == 20
    assert len(stack) == 2

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(5)
    assert stack.is_empty() == False
    
    stack.pop()
    assert stack.is_empty() == True

def test_stack_length():
    stack = Stack()
    assert len(stack) == 0
    
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    
    stack.pop()
    assert len(stack) == 1

def test_stack_multiple_operations():
    stack = Stack()
    for i in range(5):
        stack.push(i)
    assert len(stack) == 5
    assert stack.peek() == 4
    assert stack.pop() == 4
    assert stack.pop() == 3
    stack.push(100)
    assert stack.pop() == 100
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == 0
    assert stack.is_empty() == True