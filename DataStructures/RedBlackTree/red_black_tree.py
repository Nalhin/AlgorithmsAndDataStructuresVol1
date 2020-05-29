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

    @property
    def is_valid(self):
        try:
            self.validate_tree_color(self.root)
            self.recursive_black_height(self.root)
            return True
        except ValueError:
            return False

    def validate_tree_color(self, node, color=Color.BLACK):
        if color == Color.RED and node.color == Color.RED:
            raise ValueError("Invalid node color")

        if node == NULL:
            return True

        left_side_valid = self.validate_tree_color(node.left, node.color)
        right_side_valid = self.validate_tree_color(node.right, node.color)

        return left_side_valid and right_side_valid

    def recursive_black_height(self, node):
        if node == NULL:
            return 0

        left_count = self.recursive_black_height(node.left)
        right_count = self.recursive_black_height(node.right)

        if left_count != right_count:
            raise ValueError("Invalid black height")

        return left_count + (1 if node.color == Color.BLACK else 0)

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

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != NULL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == NULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != NULL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == NULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

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

        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                if node.parent.parent.right.color == Color.RED:
                    node.parent.color = Color.BLACK
                    node.parent.parent.right.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                if node.parent.parent.left.color == Color.RED:
                    node.parent.color = Color.BLACK
                    node.parent.parent.left.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = Color.BLACK
