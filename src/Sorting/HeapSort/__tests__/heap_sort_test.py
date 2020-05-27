from random import randint

from src.Sorting.HeapSort.heap_sort import heap_sort, build_max_heap


class TestHeapSort:
    def test_build_max_heap(self):
        """should build max heap correctly"""
        initial = [5, 13, 2, 25, 7, 17, 20, 8, 4]
        expected = [25, 13, 20, 8, 7, 17, 2, 5, 4]

        build_max_heap(initial)

        assert initial == expected

    def test_sorts_an_array(self):
        """should sort an array of predefined values"""
        initial = [1, 3, 2, 5, 6, 2, 4, 2, 8]
        expected = sorted(initial)

        heap_sort(initial)

        assert initial == expected

    def test_sorts_array_with_random_values(self):
        """should sort an array consisting of random values"""
        initial = [randint(1, 1000) for _ in range(100)]
        expected = sorted(initial)

        heap_sort(initial)

        assert initial == expected
