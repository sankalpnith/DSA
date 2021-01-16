class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # first create a max heap
        h = MaxHeap()
        h.build_heap(nums)
        for i in range(k):
            maxi = h.delete_max()
        return maxi
        
class MaxHeap:
        
        def __init__(self):
            self.data=[]
            self.size=0

        def left_index(self, index):
            index = 2*index +1
            return -1 if index >=self.size else index
        
        def right_index(self, index):
            index = 2*index +2
            return -1 if index >=self.size else index
        
        def build_heap(self, arr):
            self.data.extend(arr)
            self.size = len(arr)
            index = (self.size-1)//2
            while index >=0:
                self.percolate_down(index)
                index -=1

        def delete_max(self):
            maxi = self.data[0]
            self.data[0] = self.data.pop()
            self.size -=1
            self.percolate_down(0)
            return maxi

        def percolate_down(self, index):
            left_index = self.left_index(index)
            right_index = self.right_index(index)
            
            max_index = index
            if left_index != -1 and self.data[max_index] < self.data[left_index]:
                max_index = left_index
                
            
            if right_index !=-1 and self.data[max_index] < self.data[right_index]:
                max_index = right_index
            if max_index!= index:
                self.data[max_index], self.data[index] = self.data[index], self.data[max_index]
                self.percolate_down(max_index)
