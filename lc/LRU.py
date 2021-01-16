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


