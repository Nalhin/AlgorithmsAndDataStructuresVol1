from random import randint

from src.Sorting.RadixSort.radix_sort import radix_sort


class TestRadixSort:
    def test_sorts_an_array(self):
        """should sort an array of predefined values"""
        initial = [1, 3, 2, 5, 6, 2, 4, 2, 8]
        expected = sorted(initial)

        radix_sort(initial)

        assert initial == expected

    def test_sorts_array_with_random_values(self):
        """should sort an array consisting of random values"""
        initial = [randint(1, 100) for _ in range(100)]
        expected = sorted(initial)

        radix_sort(initial)

        assert initial == expected
