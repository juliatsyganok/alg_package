import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from sorts import bubble_sort, quick_sort, bucket_sort, counting_sort, radix_sort, heap_sort


def test_bubble_sort_basic():
    assert bubble_sort([3, 1, 4, 2]) == [1, 2, 3, 4]


def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]

def test_quick_sort_basic():
    assert quick_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

def test_quick_sort_large_array():
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6, 0]
    assert quick_sort(arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_counting_sort_basic():
    assert counting_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

def test_counting_sort_with_duplicates():
    assert counting_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_counting_sort_single_element():
    assert counting_sort([5]) == [5]

def test_radix_sort_basic():
    assert radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_same_length():
    assert radix_sort([123, 456, 789, 234, 567]) == [123, 234, 456, 567, 789]

def test_heap_sort_basic():
    assert heap_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

