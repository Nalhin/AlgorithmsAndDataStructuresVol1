from typing import Any


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Returns whether the list is empty"""
        return not self.head

    def _search(self, val: int) -> Node:
        """Returns node with given key from the list"""
        curr_node = self.head

        while curr_node and curr_node.val != val:
            curr_node = curr_node.next

        return curr_node

    def get_at(self, index: int) -> Any:
        """Get value present at given position"""
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

    def insert(self, val: int) -> None:
        """Adds node with given key at the beginning of the list"""
        prev_head = self.head
        node = Node(val, next=prev_head)
        if prev_head:
            prev_head.prev = node

        self.head = node

    def push(self, val) -> None:
        """Adds node with a given value at the end of the list"""
        curr_node = self.head
        node = Node(val, next=None, prev=curr_node)

        if not curr_node:
            self.head = node
            return

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = node

    def delete(self, key: int) -> None:
        """Removes first occurrence of a given key from the list"""
        node = self.head
        node_to_delete = self._search(key)
        if node_to_delete:
            self._remove_node(node)

    def _remove_node(self, node: Node) -> None:
        """Removes given node from the list"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
