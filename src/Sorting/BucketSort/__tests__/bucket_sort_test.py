from random import random

from src.Sorting.BucketSort.bucket_sort import bucket_sort


class TestBucketSort:

    def test_sorts_an_array(self):
        """should sort an array of predefined values"""
        initial = [.1, .3, .2, .5, .6, .2, .4, .2, .8]
        expected = sorted(initial)

        result = bucket_sort(initial)

        assert result == expected

    def test_sorts_array_with_random_values(self):
        """should sort an array consisting of random values"""
        initial = [random() for _ in range(100)]
        expected = sorted(initial)

        result = bucket_sort(initial)

        assert result == expected
