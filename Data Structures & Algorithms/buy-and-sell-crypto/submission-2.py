class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This question is a two-pointer question.
        # One pointer is going to be your buy price. One will be your sell price.
        # It is important that you buy low, sell high. 
        # This lowpoint/buyprice can change if there's a lower value later on.

        #Start by creating the two pointers
        left = 0 # Buy price
        right = 0 # Sell price
        profit = 0 # profit amount
        max_profit = 0 # Max profit
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[right] < prices[left]:
                left = right
            right+=1
        return max_profit
