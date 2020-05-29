import pytest

from DataStructures.PriorityQueue.max_priority_queue import MaxPriorityQueue


@pytest.fixture()
def priority_queue():
    return MaxPriorityQueue()


class TestMaxPriorityQueue:
    def test_insert(self, priority_queue):
        """Should insert elements correctly"""
        item = 5

        priority_queue.insert(item, 10)

        assert priority_queue.maximum() == item

    def test_maximum(self, priority_queue):
        """Should return element with highest key"""
        maximum = 2

        priority_queue.insert(1, 3)
        priority_queue.insert(1, 5)
        priority_queue.insert(maximum, 10)

        assert priority_queue.maximum() == maximum

    def test_extract_max(self, priority_queue):
        """Should extract element with highest key"""
        maximum = 9
        second_max = 8

        priority_queue.insert(1, 3)
        priority_queue.insert(second_max, 5)
        priority_queue.insert(maximum, 10)

        assert priority_queue.extract_max() == maximum
        assert priority_queue.maximum() == second_max

    def test_extract_max_raises_exception(self, priority_queue):
        with pytest.raises(Exception):
            assert priority_queue.extract_max()

    def test_increase_key(self, priority_queue):
        """Should increase element's key correctly"""
        maximum = 9

        priority_queue.insert(1, 3)
        priority_queue.insert(2, 5)
        priority_queue.insert(maximum, 10)

        priority_queue.increase_key(2, 10)

        assert priority_queue.extract_max() == maximum

    def test_increase_key_raises_exception(self, priority_queue):
        priority_queue.insert(1, 3)

        with pytest.raises(Exception):
            priority_queue.increase_key(2, 1)
