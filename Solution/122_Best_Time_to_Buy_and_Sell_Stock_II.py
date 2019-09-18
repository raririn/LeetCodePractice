class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                ret = ret + prices[i] - prices[i-1]
        return ret

'''
Runtime: 72 ms, faster than 70.27% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.8 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.
'''