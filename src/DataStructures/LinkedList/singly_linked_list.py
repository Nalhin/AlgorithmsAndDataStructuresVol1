class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        """Returns node with given key from the list"""
        curr_node = self.head

        while curr_node and curr_node.key != key:
            curr_node = curr_node.next

        return curr_node

    def insert(self, key):
        """Adds node with given key at the beginning of the list"""
        node = Node(key, next=self.head)
        self.head = node

    def push(self, key):
        """Adds node with a given key at the end of the list"""
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next

        curr_node.next = Node(key)

    def delete(self, val: int) -> None:
        """Removes first occurrence of a given key from the list"""
        node = self.search(val)
        if node:
            self.remove_node(node)

    @staticmethod
    def remove_node(node: Node) -> None:
        """Removes given node from the list"""
        node.val = node.next.key
        node.next = node.next.next
