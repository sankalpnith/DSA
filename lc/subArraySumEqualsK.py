from collections import defaultdict

def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        total_sum = 0
        sub_array_count = 0
        for value in nums:
            total_sum += value
            sub_array_count += sum_dict[total_sum-k]
            sum_dict[total_sum] += 1
            
        return sub_array_count

def subarraySum1(self, nums, k) :
    sum_dict = defaultdict(int)
    total_sum = 0
    sub_array_count = 0
    for value in nums:
        total_sum += value
        if total_sum == k:
            sub_array_count += 1
        sub_array_count += sum_dict[total_sum-k]
        sum_dict[total_sum] += 1
            
    return sub_array_count

