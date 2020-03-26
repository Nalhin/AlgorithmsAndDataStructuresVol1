from typing import Any


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        """Returns whether the stack is empty

        :returns: is stack empty
        :rtype: bool
        """
        return not len(self.items)

    def size(self) -> int:
        """Returns the number of items in stack

        :returns: number of items in stack
        :rtype: int
        """
        return len(self.items)

    def push(self, item: Any) -> None:
        """Adds item to the top of the stack

        :param item: object to add
        :type item: object
        :returns: None
        """
        self.items.append(item)

    def pop(self) -> Any:
        """Removes and return top item from the stack

        :returns: removed object
        :rtype: Any
        """
        if self.is_empty():
            raise Exception("Stack underflow.")
        return self.items.pop()
