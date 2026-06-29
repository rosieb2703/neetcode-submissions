class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = []

        for i in range(len(prices)):
            future_days = prices[i:]
            max_profit = max(future_days) - prices[i]
            profit.append(max_profit)

        return max(profit)



