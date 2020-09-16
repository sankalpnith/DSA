#Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
#Each time the sliding window moves right by one position. Return the max sliding window.

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_sliding_list = []
        for i in range(len(nums)-k+1):
            maxi = nums[i]
            for j in range(1,k):
                if nums[i+j]> maxi:
                    maxi=nums[i+j]
            max_sliding_list.append(maxi)
        return max_sliding_list


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        maxWindowList = []
        start = 0
        end = k-1
        temp = start
        maxi = nums[end]
        while end<len(nums):
            if nums[start] > maxi:
                maxi = nums[start]
            start+=1
            if start==end:
                maxWindowList.append(maxi)
                end+=1
                start = temp +1
                temp = start
                if end < len(nums):
                    maxi = nums[end]
        return maxWindowList

 def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        maxWindowList = []
        queue = []
        queue.append(0)
        for i in range(1, k):
            while queue and nums[i]>nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(k,len(nums)):
            maxWindowList.append(nums[queue[0]])
            
            while queue and queue[0] <= i-k:
                queue.pop(0)
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        maxWindowList.append(nums[queue[0]])
        return maxWindowList
