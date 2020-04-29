from random import random

import pytest

from src.DataStructures.BinarySearchTree.binary_search_tree import BinarySearchTree


@pytest.fixture()
def binary_search_tree():
    return BinarySearchTree()


def populate_tree(binary_search_tree, items):
    for i in items:
        binary_search_tree.insert(i)


class TestBinarySearchTree:
    def test_inorder_tree_traversal(self, binary_search_tree):
        values = [3, 2, 12, 4, 5, 6, 2]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.inorder_tree_traversal()

        assert result == sorted(values)

    def test_inorder_tree_traversal_random_values(self, binary_search_tree):
        values = [random() for _ in range(100)]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.inorder_tree_traversal()

        assert result == sorted(values)

    def test_minimum(self, binary_search_tree):
        values = [3, 2, 12, 4, 5, 6, 2]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.minimum()

        assert result == min(values)

    def test_minimum_random_values(self, binary_search_tree):
        values = [random() for _ in range(100)]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.minimum()

        assert result == min(values)

    def test_maximum(self, binary_search_tree):
        values = [3, 2, 12, 4, 5, 6, 2]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.maximum()

        assert result == max(values)

    def test_maximum_random_values(self, binary_search_tree):
        values = [random() for _ in range(100)]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.maximum()

        assert result == max(values)

    def test_tree_successor(self, binary_search_tree):
        val = 4
        expected = 5
        values = [3, expected, 2, 12, 6, 2, val]
        populate_tree(binary_search_tree, values)

        node = binary_search_tree.search(val)
        result = binary_search_tree.tree_successor(node)

        assert result.val == expected

    def test_tree_predecessor(self,binary_search_tree):
        val = 5
        expected = 4
        values = [3, expected, 2, 12, 6, 2, val]
        populate_tree(binary_search_tree, values)

        node = binary_search_tree.search(val)
        result = binary_search_tree.tree_predecessor(node)

        assert result.val == expected

    def test_search(self, binary_search_tree):
        searched_value = 12
        values = [3, 2, searched_value, 4, 5, 6, 2]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.search(searched_value)

        assert result.val == searched_value

    def test_search_random_values(self, binary_search_tree):
        values = [random() for _ in range(100)]
        searched_value = values[20]
        populate_tree(binary_search_tree, values)

        result = binary_search_tree.search(searched_value)

        assert result.val == searched_value

    def test_insert(self, binary_search_tree):
        values = [3, 2, 12, 4, 5, 6, 2]

        populate_tree(binary_search_tree, values)
        result = binary_search_tree.inorder_tree_traversal()

        assert result == sorted(values)

    def test_insert_random_values(self, binary_search_tree):
        values = [random() for _ in range(100)]

        populate_tree(binary_search_tree, values)
        result = binary_search_tree.inorder_tree_traversal()

        assert result == sorted(values)

    def test_delete(self,binary_search_tree):
        values = [3, 2, 12, 4, 5, 6, 2]
        populate_tree(binary_search_tree, values)

        for i in values[3:]:
            binary_search_tree.delete(i)

        assert binary_search_tree.inorder_tree_traversal() == sorted(values[:-4])