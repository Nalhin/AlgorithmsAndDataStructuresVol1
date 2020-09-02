from typing import Any


class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        """Returns whether the queue is empty"""
        return not len(self.data)

    def size(self) -> int:
        """Returns queue size"""
        return len(self.data)

    def enqueue(self, item) -> None:
        """Adds item to the queue"""
        self.data.insert(0, item)

    def dequeue(self) -> Any:
        """Removes and returns last item from the queue"""
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.data.pop()
