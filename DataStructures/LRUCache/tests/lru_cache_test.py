import pytest

from DataStructures.LRUCache.lru_cache import LRUCache


@pytest.fixture()
def lru_cache():
    return LRUCache(2)


class TestLRUCache:
    def test_put_and_get(self, lru_cache):
        key = 2
        val = 1

        lru_cache.put(key, val)
        result = lru_cache.get(key)

        assert val == result

    def test_operation_chain(self, lru_cache):
        expected = [1, -1, -1, 3, 4]
        result = []

        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        result.append(lru_cache.get(1))
        lru_cache.put(3, 3)
        result.append(lru_cache.get(2))
        lru_cache.put(4, 4)
        result.append(lru_cache.get(1))
        result.append(lru_cache.get(3))
        result.append(lru_cache.get(4))

        assert expected == result

    def test_operation_chain_with_put_removal(self, lru_cache):
        expected = [-1, -1, 2, 6]
        result = []

        result.append(lru_cache.get(2))
        lru_cache.put(2, 6)
        result.append(lru_cache.get(1))
        lru_cache.put(1, 5)
        lru_cache.put(1, 2)
        result.append(lru_cache.get(1))
        result.append(lru_cache.get(2))

        assert expected == result
