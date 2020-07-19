class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i,j = 0, 1
        while i < len(prices):
            while j < len(prices):
                if prices[j] > prices[i]:
                    j += 1
                else:
                    prices[i] -= prices[j]
                    i += 1
                    j = i + 1
            i += 1
            j = i + 1
        return prices

'''
Runtime: 100 ms, faster than 16.09% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
'''