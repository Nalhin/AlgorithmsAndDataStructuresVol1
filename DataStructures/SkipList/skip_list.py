from random import random
from typing import Optional, List


class Node:
    val: int
    next: List[Optional['Node']]

    def __init__(self, val: int, level: int):
        self.val = val
        self.next = [None] * (level + 1)


class SkipList:
    head: Optional[Node]
    prob: float
    max_level: int
    level: int

    def __init__(self, prob=0.5, max_level=16):
        self.prob = prob
        self.max_level = max_level
        self.head = Node(-1, self.max_level)
        self.level = 0

    def get_random_level(self) -> int:
        lvl = 0
        while lvl < self.max_level and random() < self.prob:
            lvl += 1
        return lvl

    def search(self, val: int) -> Optional[int]:
        curr = self.head
        for level in range(self.level, -1, -1):
            while curr.next[level] is not None and curr.next[level].val < val:
                curr = curr.next[level]
        curr = curr.next[0]
        if curr and curr.val == val:
            return curr.val
        else:
            return None

    def _gen_updates(self, curr: Node, val: int) -> [List[Optional[Node]], Node]:
        update_cache = [None] * self.max_level
        for level in range(self.level, -1, -1):
            while curr.next[level] is not None and curr.next[level].val < val:
                curr = curr.next[level]
            update_cache[level] = curr
        return update_cache, curr

    def insert(self, val: int) -> None:
        curr = self.head
        update_cache, curr = self._gen_updates(curr, val)
        curr = curr.next[0]
        if curr is None or curr.val != val:
            level = self.get_random_level()
            if level > self.level:
                for i in range(self.level + 1, level + 1):
                    update_cache[i] = self.head
                self.level = level

            node = Node(val, level)
            for lvl in range(level + 1):
                node.next[lvl] = update_cache[lvl].next[lvl]
                update_cache[lvl].next[lvl] = node

    def remove(self, val: int) -> None:
        curr = self.head
        update_cache, curr = self._gen_updates(curr, val)
        curr = curr.next[0]

        if curr is not None and curr.val == val:
            for lvl in range(self.level + 1):
                if update_cache[lvl].next[lvl] != curr:
                    break
                update_cache[lvl].next[lvl] = curr.next[lvl]
