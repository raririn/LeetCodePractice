class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt, floor
        from functools import lru_cache
        
        @lru_cache(n)
        def wrapper(n):
            if n <= 0:
                return float('inf')
            floored_root = floor(sqrt(n))
            if n == floored_root * floored_root:
                return 1
            return min([1+wrapper(n-i*i) for i in range(1, floored_root+1)])
        
        return wrapper(n)

'''
Runtime: 4132 ms, faster than 49.93% of Python3 online submissions for Perfect Squares.
Memory Usage: 40.8 MB, less than 5.56% of Python3 online submissions for Perfect Squares.
'''