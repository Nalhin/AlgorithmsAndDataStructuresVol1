import pytest

from src.DataStructures.LinkedList.singly_linked_list import SinglyLinkedList


@pytest.fixture()
def singly_linked_list():
    return SinglyLinkedList()


class TestSinglyLinkedList:
    def test_is_empty(self, singly_linked_list):
        result = singly_linked_list.is_empty()

        assert result

    def test_size(self, singly_linked_list):
        singly_linked_list.add_first(1)
        singly_linked_list.add_first(2)
        singly_linked_list.add_first(3)

        result = singly_linked_list.size()

        assert result == 3

    def test_get_first(self, singly_linked_list):
        item = 4
        singly_linked_list.add_first(1)
        singly_linked_list.add_first(item)

        result = singly_linked_list.get_first()

        assert result == item

    def test_get_at(self, singly_linked_list):
        item = 2
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(item)
        singly_linked_list.add_first(3)

        result = singly_linked_list.get_at(1)

        assert result == item

    def test_get_at_empty_list(self, singly_linked_list):
        with pytest.raises(Exception):
            assert singly_linked_list.get_at(0)

    def test_get_at_out_of_bounds(self, singly_linked_list):
        singly_linked_list.add_first(1)

        with pytest.raises(Exception):
            assert singly_linked_list.get_at(1)

    def test_get_last(self, singly_linked_list):
        item = 2
        singly_linked_list.add_first(item)
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(3)

        result = singly_linked_list.get_last()

        assert result == item

    def test_get_last_empty_list(self, singly_linked_list):
        with pytest.raises(Exception):
            assert singly_linked_list.get_at(0)

    def test_add_at(self, singly_linked_list):
        item = 2
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(3)

        singly_linked_list.add_at(1, item)

        assert singly_linked_list.get_at(1) == item

    def test_add_at_first(self, singly_linked_list):
        item = 2
        singly_linked_list.add_at(0, item)

        assert singly_linked_list.get_at(0) == item

    def test_add_at_out_of_bounds(self, singly_linked_list):
        with pytest.raises(Exception):
            assert singly_linked_list.add_at(2, 1)

    def test_add_last(self, singly_linked_list):
        item = 2
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(3)

        singly_linked_list.add_last(item)

        assert singly_linked_list.get_last() == item

    def test_index_of(self, singly_linked_list):
        item = 2
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(item)
        singly_linked_list.add_first(3)

        result = singly_linked_list.index_of(item)

        assert result == 1

    def test_delete_first(self, singly_linked_list):
        item = 4
        singly_linked_list.add_first(item)
        singly_linked_list.add_first(3)

        singly_linked_list.delete_first()

        assert singly_linked_list.get_first() == item

    def test_delete_at(self, singly_linked_list):
        singly_linked_list.add_first(3)
        singly_linked_list.add_first(3)

        singly_linked_list.delete_at(1)

        with pytest.raises(Exception):
            assert singly_linked_list.get_at(1)

    def test_clear(self, singly_linked_list):
        singly_linked_list.add_first(1)
        singly_linked_list.add_first(1)

        singly_linked_list.clear()

        assert not singly_linked_list.size()
