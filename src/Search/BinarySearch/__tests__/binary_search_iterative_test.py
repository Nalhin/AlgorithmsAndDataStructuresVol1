from src.Search.BinarySearch.binary_search_iterative import (
    binary_search_iterative,
)


class TestBinarySearchIterative:
    def test_element_found(self):
        array = [1, 2, 3, 4, 6, 7]
        expected = 3

        index = binary_search_iterative(array, 4)

        assert index == expected

    def test_element_not_found(self):
        array = [1, 2, 3, 4, 6, 7]
        expected = None

        index = binary_search_iterative(array, 10)

        assert index == expected
