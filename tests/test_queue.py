import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from queue import Queue

def test_queue_initialization():
    queue = Queue()
    assert len(queue) == 0
    assert queue.is_empty() == True

def test_queue_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    assert len(queue) == 3
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert len(queue) == 0

def test_queue_front():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    
    assert queue.front() == 10
    assert len(queue) == 2  

def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    
    queue.enqueue(5)
    assert queue.is_empty() == False
    
    queue.dequeue()
    assert queue.is_empty() == True

def test_queue_length():
    queue = Queue()
    assert len(queue) == 0
    
    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2
    
    queue.dequeue()
    assert len(queue) == 1

def test_queue_fifo_behavior():
    queue = Queue()
    items = [1, 2, 3, 4, 5]
    for item in items:
        queue.enqueue(item)
    for expected in items:
        assert queue.dequeue() == expected

def test_queue_multiple_operations():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.front() == 2
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.is_empty() == True