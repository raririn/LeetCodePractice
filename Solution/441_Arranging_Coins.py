from math import sqrt, floor
class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(floor(sqrt(2*n)), 0, -1):
            if i * (i + 1) // 2 <= n:
                return i
        return 0

'''
Runtime: 44 ms, faster than 66.88% of Python3 online submissions for Arranging Coins.
Memory Usage: 14 MB, less than 5.00% of Python3 online submissions for Arranging Coins.
'''