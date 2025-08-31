class Solution:
    def maxProfit(self, prices):
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
        
        return profit2
