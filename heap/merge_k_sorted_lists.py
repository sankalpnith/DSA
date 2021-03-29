# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
        node = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.size -= 1
        self.percolate_down(0)
        return node

    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        if parent_index != -1 and self.arr[index].val < self.arr[parent_index].val:
            self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
            self.percolate_up(parent_index)

    def percolate_down(self, index):
        min_index = index
        left_index = self.left_index(index)
        right_index = self.right_index(index)
        if left_index != -1 and self.arr[left_index].val < self.arr[min_index].val:
            min_index = left_index
        if right_index != -1 and self.arr[right_index].val < self.arr[min_index].val:
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = result = None
        lists = [node for node in lists if node]

        heap = Heap(lists, len(lists))
        heap.create_heap()
        while heap.size != 0:
            print(heap.size)
            node = heap.delete()
            if not result:
                head = result = node
            else:
                result.next = node
                result = result.next

            if node and node.next:
                heap.insert(node.next)
        return head
