from typing import Any


class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        """Returns whether the queue is empty

        :returns: is queue empty
        :rtype: bool
        """
        return not len(self.data)

    def size(self) -> int:
        """Returns queue size

        :returns: item
        :rtype: int
        """
        return len(self.data)

    def enqueue(self, item) -> None:
        """Adds item to the queue

        :returns: none
        :rtype: None
        """
        self.data.insert(0, item)

    def dequeue(self) -> Any:
        """Removes and returns last item from the queue

        :returns: last item
        :rtype: Any
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.data.pop()
