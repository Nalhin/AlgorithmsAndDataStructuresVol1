from typing import Any


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return not self.head

    def size(self) -> int:
        curr_node = self.head
        counter = 0
        while curr_node:
            counter += 1
            curr_node = curr_node.next

        return counter

    def get_first(self) -> Any:
        return self.head.val

    def get_at(self, index: int) -> Any:
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
        if self.is_empty():
            raise IndexError("List is empty")

        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        return curr_node.val

    def add_first(self, item: Any) -> None:
        self.head = Node(item, self.head)

    def add_at(self, index: int, item: Any) -> None:

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
        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = Node(item, None)

    def index_of(self, item: Any) -> int:
        curr_node = self.head
        index = 0
        while curr_node:
            if curr_node.val == item:
                return index
            index += 1
            curr_node = curr_node.next

        return -1

    def delete_first(self) -> None:
        node = self.head
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            self.head = None

    def delete_at(self, index: int) -> None:
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
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            del curr_node
            curr_node = next_node

        self.head = None
