class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        min_cost = prices[0]
        for i in range(len(prices)):
            min_cost = min(prices[i], min_cost)
            profit = prices[i] - min_cost
            max_profit = max(max_profit, profit)     
        return max_profit