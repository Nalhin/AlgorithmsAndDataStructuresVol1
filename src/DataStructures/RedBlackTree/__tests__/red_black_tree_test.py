from random import random

import pytest

from src.DataStructures.RedBlackTree.red_black_tree import RedBlackTree


@pytest.fixture()
def red_black_tree():
    return RedBlackTree()


def populate_tree(binary_search_tree, items):
    for i in items:
        binary_search_tree.insert(i)


class TestRedBlackTree:
    def test_insert_predefined_values(self, red_black_tree):
        values = [3, 2, 12, 4, 5, 6, 2]

        populate_tree(red_black_tree, values)
        result = red_black_tree.inorder_tree_traversal()

        assert result == sorted(values)

    def test_insert_random_values(self, red_black_tree):
        values = [random() for _ in range(100)]

        populate_tree(red_black_tree, values)
        result = red_black_tree.inorder_tree_traversal()

        assert result == sorted(values)