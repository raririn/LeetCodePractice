class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxprice = 0
        maxprofit = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxprice:
                maxprice = prices[i]
            if maxprice - prices[i] > maxprofit:
                maxprofit = maxprice - prices[i]
        return maxprofit

'''
Runtime: 76 ms, faster than 55.46% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.8 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''