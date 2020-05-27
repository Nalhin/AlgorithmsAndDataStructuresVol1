from random import random

from src.Sorting.BucketSort.bucket_sort import bucket_sort


class TestBucketSort:
    def test_sorts_an_array(self):
        """should sort an array of predefined values"""
        initial = [0.1, 0.3, 0.2, 0.5, 0.6, 0.2, 0.4, 0.2, 0.8]
        expected = sorted(initial)

        result = bucket_sort(initial)

        assert result == expected

    def test_sorts_array_with_random_values(self):
        """should sort an array consisting of random values"""
        initial = [random() for _ in range(100)]
        expected = sorted(initial)

        result = bucket_sort(initial)

        assert result == expected
