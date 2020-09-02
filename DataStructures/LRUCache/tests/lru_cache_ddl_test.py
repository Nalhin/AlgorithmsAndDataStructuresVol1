import pytest

from DataStructures.LRUCache.lru_cache_ddl import LRUCacheDDL


@pytest.fixture()
def lru_cache():
    return LRUCacheDDL(2)


class TestLRUCacheDDL:
    def test_put_and_get(self, lru_cache):
        key = 2
        val = 1

        lru_cache.put(key, val)
        result = lru_cache.get(key)

        assert val == result

    def test_operation_chain(self, lru_cache):
        expected = [1, None, None, 3, 4]
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
        expected = [None, None, 2, 6]
        result = []

        result.append(lru_cache.get(2))
        lru_cache.put(2, 6)
        result.append(lru_cache.get(1))
        lru_cache.put(1, 5)
        lru_cache.put(1, 2)
        result.append(lru_cache.get(1))
        result.append(lru_cache.get(2))

        assert expected == result
