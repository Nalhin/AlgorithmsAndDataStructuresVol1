import pytest

from src.DataStructures.Queue.queue import Queue


@pytest.fixture()
def queue():
    return Queue()


class TestQueue:
    def test_is_empty(self, queue):
        result = queue.is_empty()

        assert result

    def test_size(self, queue):
        queue.enqueue(1)
        queue.enqueue(1)

        result = queue.size()

        assert result

    def test_enqueue(self, queue):
        queue.enqueue(1)

        assert not queue.is_empty()

    def test_dequeue(self, queue):
        item = 1
        queue.enqueue(1)

        result = queue.dequeue()

        assert result == item
        assert queue.is_empty()

    def test_dequeue_empty(self):
        with pytest.raises(Exception):
            assert queue.dequeue()
