import pytest

from src.DataStructures.Stack.stack import Stack


@pytest.fixture()
def stack():
    return Stack()


class TestStack:
    def test_is_empty(self, stack):
        result = stack.is_empty()

        assert result

    def test_size(self, stack):
        stack.push(1)
        stack.push(1)
        stack.push(1)

        assert stack.size() == 3

    def test_push(self, stack):
        stack.push(1)

        assert not stack.is_empty()

    def test_pop(self, stack):
        item = 1
        stack.push(item)

        result = stack.pop()

        assert result == item

    def test_pop_underflow(self, stack):
        with pytest.raises(Exception):
            assert stack.pop()
