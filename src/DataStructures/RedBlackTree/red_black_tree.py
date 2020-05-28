from enum import Enum
from typing import List


class Color(Enum):
    BLACK = 0
    RED = 1


class Node:
    def __init__(self, value, color, left=None, right=None, parent=None):
        self.val = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


NULL = Node(None, Color.BLACK)


class RedBlackTree:
    def __init__(self):
        self.root = NULL

    def inorder_tree_traversal(self) -> List:
        """returns items inserted into the tree in sorted order"""
        items = []

        self._recursive_tree_traversal(self.root, items)

        return items

    def _recursive_tree_traversal(self, node, items):
        """traversals the tree and appends values in sorted order"""
        if node == NULL:
            return

        self._recursive_tree_traversal(node.left, items)
        items.append(node.val)
        self._recursive_tree_traversal(node.right, items)

    def _left_rotate(self, rotated):
        to_rotate = rotated.left
        rotated.right = to_rotate.left

        if rotated.left != NULL:
            rotated.left.parent = rotated

        if to_rotate.parent == NULL:
            self.root = rotated
        elif to_rotate.parent.left == to_rotate:
            to_rotate.parent.left = rotated
        else:
            to_rotate.parent.right = rotated

        rotated.left = to_rotate
        to_rotate.parent = rotated

    def _right_rotate(self, rotated):
        to_rotate = rotated.left
        to_rotate.left = rotated.right

        if rotated.right != NULL:
            rotated.right.parent = rotated

        if rotated.parent == NULL:
            self.root = rotated
        elif rotated.parent.left == to_rotate:
            rotated.parent.left = rotated
        else:
            rotated.parent.right = rotated

        rotated.left = to_rotate
        to_rotate.parent = rotated

    def insert(self, val):
        node = self.root
        parent = NULL

        while node != NULL:
            parent = node
            if node.val > val:
                node = node.left
            else:
                node = node.right

        new_node = Node(val, Color.RED, left=NULL, right=NULL, parent=parent)

        if parent == NULL:
            self.root = new_node
        elif parent.val > new_node.val:
            parent.left = new_node
        else:
            parent.right = new_node

    def _insert_fixup(self, node):
        while node.parent.color == Color.RED:
            grand_parent = node.parent.parent
            if node.parent == grand_parent.left:
                if grand_parent.right.color == Color.RED:
                    node.parent.color = Color.BLACK
                    grand_parent.right.color = Color.BLACK
                    grand_parent.color = Color.BLACK
                elif node == node.parent.right:
                    node = node.parent
                    self._left_rotate(node)

                node.parent.color = Color.BLACK
                grand_parent.color = Color.RED
                self._right_rotate(grand_parent)
            else:
                if grand_parent.left.color == Color.RED:
                    node.parent.color = Color.BLACK
                    grand_parent.left.color = Color.BLACK
                    grand_parent.color = Color.BLACK
                elif node == node.parent.left:
                    node = node.parent
                    self._right_rotate(node)

                node.parent.color = Color.BLACK
                grand_parent.color = Color.RED
                self._left_rotate(grand_parent)

        self.root = Color.BLACK
