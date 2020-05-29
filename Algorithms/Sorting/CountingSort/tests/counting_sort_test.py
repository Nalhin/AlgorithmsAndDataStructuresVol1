from random import randint

from Algorithms.Sorting.CountingSort.counting_sort import counting_sort


class TestCountingSort:
    def test_sorts_an_array(self):
        """should sort an array of predefined values"""
        initial = [1, 3, 2, 5, 6, 2, 4, 2, 8]
        expected = sorted(initial)

        result = counting_sort(initial, 10)

        assert result == expected

    def test_sorts_array_with_random_values(self):
        """should sort an array consisting of random values"""
        initial = [randint(1, 100) for _ in range(100)]
        expected = sorted(initial)

        result = counting_sort(initial, 110)

        assert result == expected
