# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit += price - min_price
            min_price = price
    return max_profit