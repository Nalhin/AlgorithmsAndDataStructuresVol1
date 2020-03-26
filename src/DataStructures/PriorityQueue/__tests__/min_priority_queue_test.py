import pytest

from src.DataStructures.PriorityQueue.min_priority_queue import MinPriorityQueue


@pytest.fixture()
def priority_queue():
    return MinPriorityQueue()


class TestMinPriorityQueue:
    def test_insert(self, priority_queue):
        """Should insert elements correctly"""
        item = 5

        priority_queue.insert(item, 10)

        assert priority_queue.minimum() == item

    def test_minimum(self, priority_queue):
        """Should return element with highest key"""
        minimum = 2

        priority_queue.insert(1, 3)
        priority_queue.insert(1, 5)
        priority_queue.insert(minimum, 1)

        assert priority_queue.minimum() == minimum

    def test_extract_min(self, priority_queue):
        """Should extract element with highest key"""
        minimum = 9
        second_min = 8

        priority_queue.insert(1, 5)
        priority_queue.insert(second_min, 2)
        priority_queue.insert(minimum, 1)

        assert priority_queue.extract_min() == minimum
        assert priority_queue.minimum() == second_min

    def test_extract_min_raises_exception(self, priority_queue):
        with pytest.raises(Exception):
            assert priority_queue.extract_min()

    def test_decrease_key(self, priority_queue):
        """Should increase element's key correctly"""
        minimum = 9

        priority_queue.insert(1, 4)
        priority_queue.insert(2, 5)
        priority_queue.insert(minimum, 10)

        priority_queue.decrease_key(2, 1)

        assert priority_queue.extract_min() == minimum

    def test_decrease_key_raises_exception(self, priority_queue):
        priority_queue.insert(1, 3)

        with pytest.raises(Exception):
            priority_queue.increase_key(2, 5)
