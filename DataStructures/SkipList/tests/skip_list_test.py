import pytest
from typing import List

from DataStructures.SkipList.skip_list import SkipList


@pytest.fixture()
def skip_list():
    return SkipList()


def add_multiple(sl: SkipList, items: List[int]):
    for item in items:
        sl.insert(item)


class TestSkipList:
    def test_search_present(self, skip_list):
        items = [1, 3, 4, 2, 5, 4]
        searched = items[3]
        add_multiple(skip_list, items)

        result = skip_list.search(searched)

        assert result == searched

    def test_search_missing(self, skip_list):
        items = [1, 3, 2, 5, ]
        add_multiple(skip_list, items)

        result = skip_list.search(4)

        assert result is None

    def test_insert(self, skip_list):
        items = [1, 3, 4, 2, 5, 4]
        add_multiple(skip_list, items)

        for item in items:
            assert skip_list.search(item) == item

    def test_remove(self, skip_list):
        items = [1, 3, 4, 2, 5]
        add_multiple(skip_list, items)

        for item in items:
            skip_list.remove(item)
            result = skip_list.search(item)

            assert result is None
