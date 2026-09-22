class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        buy= prices[0]

        for p in range(1,len(prices)):
            buy=min(buy,prices[p])
            profit= max(profit, prices[p]-buy)
        
        return profit
    
