import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from binary_search import binary_search_iterative, binary_search_recursive


def test_binary_search_linear_element_found():
    array = [1, 2, 3, 4, 6, 7]
    expected = 3

    index = binary_search_iterative(array, 4)

    assert index == expected


def test_binary_search_linear_element_not_found():
    array = [1, 2, 3, 4, 6, 7]
    expected = None

    index = binary_search_iterative(array, 10)

    assert index == expected


def test_binary_search_recursive_element_found():
    array = [1, 2, 3, 4, 6, 7]
    expected = 3

    index = binary_search_recursive(array, 4)

    assert index == expected


def test_binary_search_recursive_element_not_found():
    array = [1, 2, 3, 4, 6, 7]
    expected = None

    index = binary_search_recursive(array, 10)

    assert index == expected
