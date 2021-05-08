# https://leetcode.com/problems/jump-game/

def canJump(self, nums: List[int]) -> bool:
    last_good_position = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_good_position:
            last_good_position = i
    return last_good_position == 0