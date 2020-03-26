class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def search(self, val: int) -> Node:
        """Returns node with given key from the list"""
        curr_node = self.head

        while curr_node and curr_node.key != val:
            curr_node = curr_node.next

        return curr_node

    def insert(self, val: int) -> None:
        """Adds node with given key at the beginning of the list"""
        prev_head = self.head
        node = Node(val, next=prev_head)
        if prev_head:
            prev_head.prev = node

        self.head = node

    def push(self, val):
        """Adds node with a given value at the end of the list"""
        head = self.head

        while head.next:
            head = head.next

        node = Node(val, next=None, prev=head)

        head.next = node

    def delete(self, key: int) -> None:
        """Removes first occurrence of a given key from the list"""
        node = self.head
        node_to_delete = self.search(key)
        if node_to_delete:
            self.remove_node(node)

    def remove_node(self, node: Node) -> None:
        """Removes given node from the list"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
