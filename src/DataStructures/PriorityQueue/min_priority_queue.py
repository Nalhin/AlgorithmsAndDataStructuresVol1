from math import inf


class Node:
    def __init__(self, key, item=None):
        self.key = key
        self.item = item


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, key):
        """Insert item with its key into priority queue"""
        self.heap.append(Node(inf, item))
        self.decrease_key(len(self.heap) - 1, key)

    def minimum(self):
        """Returns item with highest key"""
        return self.heap[0].item

    def extract_min(self):
        """Extracts the item with smallest key"""
        if not len(self.heap):
            raise Exception("Heap underflow")

        max_value = self.minimum()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._min_heapify(0)
        return max_value

    def decrease_key(self, i, key):
        """Increase value of element's key"""
        if key > self.heap[i].key:
            raise Exception("New key is larger than current key")

        self.heap[i].key = key
        parent = self._get_parent_index(i)
        while i and self.heap[parent].key > self.heap[i].key:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = self._get_parent_index(i)

    def _min_heapify(self, i):
        """Maintains min heap property"""
        heap_size = len(self.heap) - 1
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i

        if left < heap_size and self.heap[left].key < self.heap[smallest].key:
            smallest = left

        if right < heap_size and self.heap[right].key < self.heap[smallest].key:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    @staticmethod
    def _get_parent_index(i):
        parent = (i - 1) // 2
        return parent if parent > 0 else 0
