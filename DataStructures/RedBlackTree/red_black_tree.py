from enum import Enum
from typing import Union, List, Optional


class Color(Enum):
    BLACK = 0
    RED = 1


class Node:
    def __init__(self, value: Optional[int], color: Color, left=None, right=None, parent=None):
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
    def is_valid(self) -> bool:
        """returns a value indicating whether all red-black tree properties are satisfied."""
        try:
            self.validate_tree_color(self.root)
            self.recursive_black_height(self.root)
            return True
        except ValueError:
            return False

    def validate_tree_color(self, node: Node, color=Color.BLACK) -> bool:
        """returns whether tree color property was validated"""
        if color == Color.RED and node.color == Color.RED:
            raise ValueError("Invalid node color")

        if node == NULL:
            return True

        left_side_valid = self.validate_tree_color(node.left, node.color)
        right_side_valid = self.validate_tree_color(node.right, node.color)

        return left_side_valid and right_side_valid

    def recursive_black_height(self, node: Node) -> int:
        """returns and validates tree height"""
        if node == NULL:
            return 0

        left_count = self.recursive_black_height(node.left)
        right_count = self.recursive_black_height(node.right)

        if left_count != right_count:
            raise ValueError("Invalid black height")

        return left_count + (1 if node.color == Color.BLACK else 0)

    def inorder_tree_traversal(self) -> List[Node]:
        """returns items inserted into the tree in sorted order"""
        items = []

        self._recursive_tree_traversal(self.root, items)

        return items

    def _recursive_tree_traversal(self, node: Node, items: List[Node]) -> None:
        """traversals the tree and appends values in sorted order"""
        if node == NULL:
            return

        self._recursive_tree_traversal(node.left, items)
        items.append(node.val)
        self._recursive_tree_traversal(node.right, items)

    def _left_rotate(self, x: Node) -> None:
        """rotates node x left"""
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

    def _right_rotate(self, x: Node) -> None:
        """rotates node x right"""
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

    def insert(self, val: int) -> None:
        """inserts value into the tree"""
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

    def _insert_fixup(self, node: Node) -> None:
        """preserves RBT properties after insert"""
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

    def search(self, val: int) -> Node:
        """returns the first occurrence of a node with a given value """
        node = self.root
        while node and not node.val == val:
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return node

    def _replace(self, u: Node, v: Node) -> None:
        """replaces node in the tree with the given one"""
        if u.parent == NULL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def remove(self, val: int) -> None:
        """removes a first occurrence of given value from the tree"""
        node = self.search(val)

        if node:
            self.delete(node)

    def delete(self, node: Node) -> None:
        """remove given node from the tree"""
        original_color = node.color
        if node.left != NULL:
            x = node.right
            self._replace(node, node.right)
        elif node.right == NULL:
            x = node.left
            self._replace(node, node.left)
        else:
            y = self._tree_minimum(node.right)
            x = y.right
            if y.parent == node:
                y.parent = y
            else:
                self._replace(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._replace(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if original_color == Color.BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, node: Node):
        """preserves RBG properties post delete"""
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                w = node.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._left_rotate(node.parent)
                    w = node.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    node = node.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                w = node.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._right_rotate(node.parent)
                    w = node.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    node = node.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = Color.BLACK

    @staticmethod
    def _tree_minimum(node: Node) -> Node:
        """finds a node with the lowest value present in the tree"""
        while node.left:
            node = node.left
        return node
