def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    two_sum_dict = collections.defaultdict(int)
    count = 0
    for i in range(len(nums) - 1):

        for j in range(i + 1, len(nums)):
            tmp_sum = nums[i] + nums[j]

            if tmp_sum < target:
                count += two_sum_dict[target - tmp_sum]

        for j in range(i):
            if nums[i] + nums[j] < target:
                two_sum_dict[nums[i] + nums[j]] += 1
    return count