#You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i and dp[i-coin]!=sys.maxsize:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        return dp[amount] if dp[amount] != sys.maxsize else -1
