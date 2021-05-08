# https://leetcode.com/problems/candy/
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

def candy(self, ratings: List[int]) -> int:
    size = len(ratings)
    count = [1 for _ in range(size)]
    for i in range(size - 1):
        if ratings[i + 1] > ratings[i]:
            count[i + 1] = 1 + count[i]
    for i in range(size - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            count[i - 1] = max(count[i - 1], 1 + count[i])
    return sum(count)