# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Node:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col


class Heap:

    def __init__(self, node_arr, size):
        self.arr = node_arr
        self.size = size

    def left_index(self, i):
        return 2 * i + 1 if 2 * i + 1 < self.size else -1

    def right_index(self, i):
        return 2 * i + 2 if 2 * i + 2 < self.size else -1

    def parent_index(self, i):
        if i <= 0 or i > self.size:
            return -1
        return (i - 1) // 2

    def insert(self, node):
        self.arr.append(node)
        self.size += 1
        self.percolate_up(self.size - 1)

    def delete(self):
        element = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.size -= 1
        self.percolate_down(0)
        return element

    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        if parent_index != -1 and self.arr[index].value < self.arr[parent_index].value:
            self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
            self.percolate_up(parent_index)

    def percolate_down(self, index):
        min_index = index
        left_index = self.left_index(index)
        right_index = self.right_index(index)
        if left_index != -1 and self.arr[left_index].value < self.arr[min_index].value:
            min_index = left_index
        if right_index != -1 and self.arr[right_index].value < self.arr[min_index].value:
            min_index = right_index
        if min_index != index:
            self.arr[min_index], self.arr[index] = self.arr[index], self.arr[min_index]
            self.percolate_down(min_index)

    def create_heap(self):
        parent_index = (self.size - 1) // 2
        while parent_index >= 0:
            self.percolate_down(parent_index)
            parent_index -= 1


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        data = []
        max_col_size = len(matrix[0])
        for i in range(len(matrix)):
            node = Node(matrix[i][0], i, 0)
            data.append(node)
        heap = Heap(data, len(matrix))
        heap.create_heap()
        while k != 0:
            node = heap.delete()
            if node.col + 1 < max_col_size:
                heap.insert(Node(matrix[node.row][node.col + 1], node.row, node.col + 1))
            k -= 1
        return node.value
