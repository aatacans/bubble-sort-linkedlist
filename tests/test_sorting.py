import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sorting_algorithms import bubble_sort
from linked_list import LinkedList

def make_ll(data):
    ll = LinkedList()
    for x in data:
        ll.add(x)
    return ll

@pytest.mark.parametrize("data, expected", [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 5, 2, 9], [2, 5, 5, 9]),
])
def test_bubble_sort_list(data, expected):
    assert bubble_sort(data.copy()) == expected

@pytest.mark.parametrize("data, expected", [
    ([], []),
    ([1], [1]),
    ([4, 2, 3], [2, 3, 4]),
    ([7, 7, 1], [1, 7, 7]),
])
def test_bubble_sort_linkedlist(data, expected):
    ll = make_ll(data)
    sorted_ll = bubble_sort(ll)
    assert list(sorted_ll) == expected
