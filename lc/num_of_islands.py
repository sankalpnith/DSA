# https://leetcode.com/problems/number-of-islands/
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

class Solution:
    def numIslands(self, grid):
        # initialize a check matrix
        check = [[False] * len(grid[0]) for i in range(len(grid))]

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not check[i][j]:
                    cnt += 1
                    self.mark(grid, check, i, j)
        return cnt

    def mark(self, grid, check, i, j):
        queue = []
        queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and check[i][j] == False:
                check[i][j] = True
                queue.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])