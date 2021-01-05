#Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0:
            return False
        target_sum = total_sum//2
        partition = [[None]*(target_sum+1) for i in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            for target in range(target_sum+1):
                if i==0 and target==0:
                    partition[i][target]=True
                elif target==0:
                    partition[i][target]=True
                elif i==0:
                    partition[i][target]=False
                elif nums[i-1]<=target:
                    partition[i][target] = partition[i-1][target] or partition[i-1][target-nums[i-1]]
                else:
                    partition[i][target] = partition[i-1][target]
        return partition[len(nums)][target_sum]
