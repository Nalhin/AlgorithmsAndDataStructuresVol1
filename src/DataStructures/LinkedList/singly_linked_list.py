from typing import Any


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Returns whether the list is empty"""
        return not self.head

    def size(self) -> int:
        """Returns list size"""
        curr_node = self.head
        counter = 0
        while curr_node:
            counter += 1
            curr_node = curr_node.next

        return counter

    def get_first(self) -> Any:
        """Returns first element"""
        return self.head.val

    def get_at(self, index: int) -> Any:
        """Returns value of element present at given index"""
        if self.is_empty():
            raise IndexError("List is empty")

        curr_index = 0
        curr_node = self.head

        while curr_node:
            if curr_index == index:
                return curr_node.val
            curr_index += 1
            curr_node = curr_node.next

        raise IndexError("List index is out of bounds")

    def get_last(self) -> Any:
        """Returns value of last element"""
        if self.is_empty():
            raise IndexError("List is empty")

        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        return curr_node.val

    def add_first(self, item: Any) -> None:
        """Adds element at start of the list"""
        self.head = Node(item, self.head)

    def add_at(self, index: int, item: Any) -> None:
        """Adds element at given position"""

        if not index:
            self.add_first(item)
            return

        curr_index = 0
        curr_node = self.head

        while curr_node:
            if curr_index == index - 1:
                curr_node.next = Node(item, curr_node.next)
                return
            curr_index += 1
            curr_node = curr_node.next

        raise IndexError("List index is out of bounds")

    def add_last(self, item: Any) -> None:
        """Appends element at the end of list"""
        curr_node = self.head
        if not curr_node:
            self.add_first(item)

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = Node(item, None)

    def index_of(self, val: Any) -> int:
        """Returns index of element with given value"""
        curr_node = self.head
        index = 0
        while curr_node:
            if curr_node.val == val:
                return index
            index += 1
            curr_node = curr_node.next

        return -1

    def delete_first(self) -> None:
        """Removes first element from the list"""
        node = self.head
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            self.head = None

    def delete_at(self, index: int) -> None:
        """Removes element present at given position"""
        if not index:
            self.delete_first()
            return

        curr_node = self.head

        while curr_node and index - 1:
            index -= 1
            curr_node = curr_node.next

        if index > 1 or not curr_node:
            raise IndexError("List index is out of bounds")

        if curr_node.next and curr_node.next.next:
            curr_node.next = curr_node.next.next
        else:
            curr_node.next = None

    def clear(self) -> None:
        """Removes all elements from the list"""
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            del curr_node
            curr_node = next_node

        self.head = None
