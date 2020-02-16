import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from linear_search import linear_search


def test_linear_search():
    array = [1, 3, 2, 4, 4, 5]
    expected = 3

    index = linear_search(array, 4)

    assert index == expected
