from random import randint

from Algorithms.Sorting.QuickSort.quick_sort_lomuto import quick_sort_lomuto


class TestQuickSortLomuto:
    def test_sorts_an_array(self):
        initial = [1, 3, 2, 5, 6, 2, 4, 2, 8]
        expected = sorted(initial)

        quick_sort_lomuto(initial)

        assert initial == expected

    def test_sorts_array_with_random_values(self):
        initial = [randint(1, 1000) for _ in range(100)]
        expected = sorted(initial)

        quick_sort_lomuto(initial)

        assert initial == expected
