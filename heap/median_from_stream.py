#https://leetcode.com/problems/find-median-from-data-stream/


class MaxHeap:

    def __init__(self):
        self.arr = []
        self.size = 0

    def left_index(self, i):
        left_index = 2 * i + 1
        return -1 if left_index >= self.size else left_index

    def right_index(self, i):
        right_index = 2 * i + 2
        return -1 if right_index >= self.size else right_index

    def parent_index(self, i):
        if i <= 0 or i > self.size:
            return -1
        return (i - 1) // 2

    def insert(self, num):
        self.arr.append(num)
        self.size += 1
        self.percolate_up(self.size - 1)

    def delete(self):
        value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.size -= 1
        self.arr.pop()
        self.percolate_down(0)
        return value

    def percolate_down(self, index):
        left_index = self.left_index(index)
        right_index = self.right_index(index)
        max_index = index
        if left_index != -1 and self.arr[left_index] > self.arr[max_index]:
            max_index = left_index
        if right_index != -1 and self.arr[right_index] > self.arr[max_index]:
            max_index = right_index
        if max_index != index:
            self.arr[max_index], self.arr[index] = self.arr[index], self.arr[max_index]
            self.percolate_down(max_index)

    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        if parent_index != -1 and self.arr[parent_index] < self.arr[index]:
            self.arr[parent_index], self.arr[index] = self.arr[index], self.arr[parent_index]
            self.percolate_up(parent_index)


class MinHeap:

    def __init__(self):
        self.arr = []
        self.size = 0

    def left_index(self, i):
        left_index = 2 * i + 1
        return -1 if left_index >= self.size else left_index

    def right_index(self, i):
        right_index = 2 * i + 2
        return -1 if right_index >= self.size else right_index

    def parent_index(self, i):
        if i <= 0 or i > self.size:
            return -1
        return (i - 1) // 2

    def insert(self, num):
        self.arr.append(num)
        self.size += 1
        self.percolate_up(self.size - 1)

    def delete(self):
        value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.size -= 1
        self.arr.pop()
        self.percolate_down(0)
        return value

    def percolate_down(self, index):
        left_index = self.left_index(index)
        right_index = self.right_index(index)
        min_index = index
        if left_index != -1 and self.arr[left_index] < self.arr[min_index]:
            min_index = left_index
        if right_index != -1 and self.arr[right_index] < self.arr[min_index]:
            min_index = right_index
        if min_index != index:
            self.arr[min_index], self.arr[index] = self.arr[index], self.arr[min_index]
            self.percolate_down(min_index)

    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        if parent_index != -1 and self.arr[parent_index] > self.arr[index]:
            self.arr[parent_index], self.arr[index] = self.arr[index], self.arr[parent_index]
            self.percolate_up(parent_index)


class MedianFinder:

    def __init__(self):
        self.lo = MaxHeap()
        self.hi = MinHeap()

    def addNum(self, num: int) -> None:
        self.lo.insert(num)
        self.hi.insert(self.lo.delete())

        if self.lo.size < self.hi.size:
            self.lo.insert(self.hi.delete())

    def findMedian(self) -> float:
        if self.lo.size == 0:
            return None
        elif self.lo.size == self.hi.size:
            return (self.lo.arr[0] + self.hi.arr[0]) / 2
        else:
            return self.lo.arr[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()