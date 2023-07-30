"""121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
------------------------------------------------------------------------------------------------------------------------------------
using two pointer approach, l for finding the new lowest price"""

class Solution():
    def maxProfit(self,prices):
        maxProf = 0
        l,r = 0,1

        while r<len(prices):
            if prices[l]<prices[r]:
                prof = prices[r]-prices[l]
                maxProf = max(maxProf,prof)
            else:
                l=r
            r+=1
        return maxProf

prices = [7,1,5,3,6,4]    
sol = Solution()
ans = sol.maxProfit(prices)
print(ans)

prices = [7,6,4,3,1]
ans = sol.maxProfit(prices)
print(ans)