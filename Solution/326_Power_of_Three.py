class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        from math import log
        from sys import float_info
        if n <= 0:
            return False
        return abs(round(log(n, 3)) - log(n, 3)) < 100*float_info.epsilon

'''
Runtime: 112 ms, faster than 20.57% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 72.16% of Python3 online submissions for Power of Three.
'''