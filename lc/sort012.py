# https://leetcode.com/problems/sort-colors/
# Sort array containing only 0,1,2

def sort(nums):
    low ,mid ,high = 0 ,0 ,len(nums ) -1
    while mid <=high:
        if nums[mid] ==0:
            nums[low] ,nums[mid] = nums[mid] ,nums[low]
            low +=1
            mid +=1
        elif nums[mid] == 1:
            mid +=1
        else:
            nums[mid] ,nums[high] = nums[high] ,nums[mid]
            high -=1


nums = [2, 0, 2, 1, 1, 0]
sort(nums)
print(nums)

