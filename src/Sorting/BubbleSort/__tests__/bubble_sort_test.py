from random import randint

from src.Sorting.BubbleSort.bubble_sort import bubble_sort


class TestBubbleSort:

    def test_sorts_an_array(self):
        initial = [1, 3, 2, 5, 6, 2, 4, 2, 8]
        expected = sorted(initial)

        bubble_sort(initial)

        assert initial == expected

    def test_sorts_array_with_random_values(self):
        initial = [randint(1, 1000) for _ in range(100)]
        expected = sorted(initial)

        bubble_sort(initial)

        assert initial == expected
