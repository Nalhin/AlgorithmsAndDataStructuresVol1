from enum import Enum


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


class RedBlackTree:
    pass
