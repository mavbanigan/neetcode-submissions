class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # Left pointer, Buying
        r = 1 # right pointer, Selling
        max_profit = 0
        while r < len(prices):
            # Check if the transaction is profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                # Super lower price found, so shift left pointer to the right pointer
                l = r
            r += 1
        return max_profit