# https://leetcode.com/problems/lru-cache/

# LRU using list/Deque and dict
# benefits insert and delete from ends is faster in deque as it is implemented as double linked list

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        # self.queue = deque()
        self.dict = {}

    def get(self, key: int) -> int:
        if self.dict.get(key) is None:
            return -1
        output = self.dict[key]
        self.queue.remove(key)
        self.queue.append(key)
        return output

    def put(self, key: int, value: int) -> None:
        # check if key exists in dict
        if self.dict.get(key) is not None:
            self.queue.remove(key)
        else:
            if len(self.queue) == self.capacity:
                del self.dict[self.queue.pop(0)]

        self.dict[key] = value
        self.queue.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Using Ordered Dict
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if self.dict.get(key) is None:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        # check if key exists in dict
        if self.dict.get(key) is not None:
            self.dict.move_to_end(key)
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last=False)

        self.dict[key] = value



# Dictionary for O(1) insertion and search. Stores key and node location
# Doubly linked list O(1) deletion, updation and insertion. Stores data and responsible for maintaining size


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.start = None
        self.end = None
        self.current_size = 0

    def get(self, key: int) -> int:
        node = self.dict.get(key)
        if not node:
            return -1
        else:
            self.remove_and_insert_at_top(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key)
        if node:
            self.remove_and_insert_at_top(node)
            node.value = value
        else:
            if self.current_size >= self.capacity:
                del self.dict[self.end.key]
                if self.start == self.end:
                    self.start, self.end = None, None
                else:
                    self.end = self.end.left
                    self.end.right.left = None
                    self.end.right = None
                    self.current_size -= 1

            node = Node(key, value)
            node.left = None
            node.right = self.start
            if self.start:
                self.start.left = node
            if not self.end:
                self.end = node
            self.start = node
            self.dict[key] = node
            self.current_size += 1

    def remove_and_insert_at_top(self, node):
        if self.start == self.end or self.start == node:
            return
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        elif node.right is None:
            self.end = node.left
        node.right = self.start
        node.left = None
        self.start.left = node
        self.start = node