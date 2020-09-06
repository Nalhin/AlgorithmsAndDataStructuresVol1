import random

import pytest

from DataStructures.RedBlackTree.red_black_tree import RedBlackTree

random.seed(123)


@pytest.fixture()
def red_black_tree():
    return RedBlackTree()


def insert_multiple(binary_search_tree, items):
    for i in items:
        binary_search_tree.insert(i)


class TestRedBlackTree:
    def test_insert(self, red_black_tree):
        data = [random.randint(0, 1000) for _ in range(100)]

        insert_multiple(red_black_tree, data)
        result = red_black_tree.inorder_tree_traversal()

        assert result == sorted(data)
        assert red_black_tree.is_valid

    def test_search(self, red_black_tree):
        data = [random.randint(0, 1000) for _ in range(100)]
        insert_multiple(red_black_tree, data)

        result = red_black_tree.search(data[20])

        assert result.val == data[20]

    def test_delete(self, red_black_tree):
        data = [5, 2, 1, 7, 2, 3, 4]
        insert_multiple(red_black_tree, data)

        red_black_tree.remove(7)
        result = red_black_tree.inorder_tree_traversal()

        assert result == [1, 2, 2, 3, 4, 5]
        assert red_black_tree.is_valid
