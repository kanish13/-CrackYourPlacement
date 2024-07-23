# 121. Best Time to Buy and Sell Stock Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        m=max(prices)
        
        for i in range(len(prices)):
                if prices[i]<m:
                    m=prices[i]
                elif prices[i]-m>p:
                    p=prices[i]-m
        return p
