"""
LeetCode 121
Difficulty: Easy

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
----------------------------------------

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,maxProfit = 0,0
        
        for sell in range(1,len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            maxProfit = max(maxProfit,prices[sell] - prices[buy])
        
        return maxProfit



