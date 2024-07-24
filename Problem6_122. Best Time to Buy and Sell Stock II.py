# 122. Best Time to Buy and Sell Stock II : Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                p=p+(prices[i]-prices[i-1])
        return p
