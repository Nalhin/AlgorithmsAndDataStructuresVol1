from typing import List


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def inorder_tree_traversal(self) -> List:
        """returns items inserted into the tree in sorted order"""
        items = []

        self._recursive_tree_traversal(self.root, items)

        return items

    def _recursive_tree_traversal(self, node, items):
        if node:
            self._recursive_tree_traversal(node.left, items)
            items.append(node.val)
            self._recursive_tree_traversal(node.right, items)

    def search(self, val):
        node = self.root
        while node and not node.val == val:
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return node

    def minimum(self):
        node = self.root
        return self._tree_minimum(node)

    @staticmethod
    def _tree_minimum(node):
        while node.left:
            node = node.left
        return node.val

    def maximum(self):
        node = self.root
        return self._tree_maximum(node)

    @staticmethod
    def _tree_maximum(node):
        while node.right:
            node = node.right
        return node.val

    def tree_successor(self, node):
        if node.right:
            return self._tree_minimum(node.right)

        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = node.parent

        return parent

    def tree_predecessor(self, node):
        if node.left:
            return self._tree_maximum(node.left)

        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    def insert(self, val):
        node = self.root

        if not node:
            self.root = Node(val)
            return

        parent = None
        while node:
            parent = node
            if node.val > val:
                node = node.left
            else:
                node = node.right

        inserted = Node(val, parent=parent)
        if parent.val > val:
            parent.left = inserted
        else:
            parent.right = inserted

