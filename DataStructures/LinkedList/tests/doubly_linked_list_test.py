import pytest

from DataStructures.LinkedList.doubly_linked_list import DoublyLinkedList


@pytest.fixture()
def doubly_linked_list():
    return DoublyLinkedList()


class TestDoublyLinkedList:
    def test_is_empty(self, doubly_linked_list):
        result = doubly_linked_list.is_empty()

        assert result

    def test_search(self, doubly_linked_list):
        item = 3

        doubly_linked_list.push(2)
        doubly_linked_list.push(item)

        result = doubly_linked_list._search(item)

        assert result.val == item

    def test_get_at(self, doubly_linked_list):
        item = 3
        doubly_linked_list.push(1)
        doubly_linked_list.push(2)
        doubly_linked_list.push(item)
        doubly_linked_list.push(1)
        doubly_linked_list.push(2)

        result = doubly_linked_list.get_at(2)

        assert result == item

    def test_insert(self, doubly_linked_list):
        item = 3
        doubly_linked_list.insert(1)
        doubly_linked_list.insert(2)

        doubly_linked_list.insert(item)
        result = doubly_linked_list.get_at(0)

        assert result == item

    def test_push(self, doubly_linked_list):
        item = 3
        doubly_linked_list.push(1)
        doubly_linked_list.push(2)
        doubly_linked_list.push(item)

        result = doubly_linked_list.get_at(2)

        assert result == item

    def test_delete(self, doubly_linked_list):
        item = 3
        expected = 2
        doubly_linked_list.push(1)
        doubly_linked_list.push(item)
        doubly_linked_list.push(expected)

        doubly_linked_list.delete(item)
        result = doubly_linked_list.get_at(1)

        assert result == expected
