class Node:
    def __init__(self, val: int or None, key: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key


class LRUCacheDDL:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, -1)
        self.tail = Node(None, -1, prev=self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int or None:
        """Returns the value associated with a given key"""
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Saves a key with its associated value"""
        if key in self.cache:
            self.cache[key].val = value
            self._move_to_tail(self.cache[key])
        else:
            if len(self.cache) >= self.capacity:
                self._remove_node(self.head.next)
            self._add_tail(key, value)

    def _remove_node(self, node: Node) -> None:
        """Removes a node from the cache"""
        node.prev.next, node.next.prev = node.next, node.prev
        del self.cache[node.key]

    def _add_tail(self, key: int, value: int) -> None:
        """Adds a node with a given key and value on the tail of ddl"""
        new = Node(value, key, next=self.tail, prev=self.tail.prev)
        self.cache[key] = new
        self.tail.prev.next = new
        self.tail.prev = new

    def _move_to_tail(self, node: Node) -> None:
        """Moves a given node to the tail of ddl"""
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
