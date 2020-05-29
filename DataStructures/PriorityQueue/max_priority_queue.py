from math import inf


class Node:
    def __init__(self, key, item=None):
        self.key = key
        self.item = item


class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, key):
        """Insert item with its key into priority queue"""
        self.heap.append(Node(-inf, item))
        self.increase_key(len(self.heap) - 1, key)

    def maximum(self):
        """Returns item with highest key"""
        return self.heap[0].item

    def extract_max(self):
        """Extracts the item with highest key"""
        if not len(self.heap):
            raise Exception("Heap underflow")

        max_value = self.maximum()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._max_heapify(0)
        return max_value

    def increase_key(self, i, key):
        """Increase value of element's key"""
        if key < self.heap[i].key:
            raise Exception("New key is smaller than current key")

        self.heap[i].key = key
        parent = self._get_parent_index(i)
        while i and self.heap[parent].key < self.heap[i].key:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = self._get_parent_index(i)

    def _max_heapify(self, i):
        """Maintains max heap property"""
        heap_size = len(self.heap) - 1
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i

        if left < heap_size and self.heap[left].key > self.heap[largest].key:
            largest = left

        if right < heap_size and self.heap[right].key > self.heap[largest].key:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(largest)

    @staticmethod
    def _get_parent_index(i):
        parent = (i - 1) // 2
        return parent if parent > 0 else 0
