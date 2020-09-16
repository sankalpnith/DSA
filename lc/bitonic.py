#You are given an integer array nums sorted in ascending order, and an integer target.
#Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#If target is found in the array return its index, otherwise, return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bitonic_index = self.find_bitonic(nums)
        print(bitonic_index)
        if nums[bitonic_index] == target:
            return bitonic_index
        
        low,high = 0, len(nums)-1
        if nums[low] <= target < nums[bitonic_index]:
            high = bitonic_index -1
        else:
            low = bitonic_index+1
        
        while low<=high:
            mid = low + (high -low)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid +1
            else:
                high = mid -1
        return -1
    
    def find_bitonic(self, nums):
        low,high = 0,len(nums) -1
        bitonic_index = 0
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] > nums[mid-1] and nums[mid]> nums[mid+1]:
                bitonic_index = mid
                break
            elif nums[mid+1]> nums[mid] and nums[mid-1] > nums[mid]:
                bitonic_index = mid-1
                break
            elif nums[mid+1] > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return 0 if bitonic_index <=0 else bitonic_index
        
