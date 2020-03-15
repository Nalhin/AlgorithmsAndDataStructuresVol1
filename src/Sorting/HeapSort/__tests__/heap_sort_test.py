from random import randint

from src.Sorting.HeapSort.heap_sort import heap_sort


class TestHeapSort:
    def test_sorts_an_array(self):
        array = [1, 3, 2, 5, 4, 6, 2, 4, 8]

        result = heap_sort(array.copy())

        assert array.sort() == result

    def test_sorts_array_with_random_values(self):
        array = [randint(1, 1000000) for _ in range(100000)]

        result = heap_sort(array.copy())

        assert array.sort() == result
