class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        profit = 0 
        buy = prices [i]
        for i in range (len(prices)):
            buy = min(buy,prices[i])
            profit = max (profit , prices[i]- buy)
        return profit