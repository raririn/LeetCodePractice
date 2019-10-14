class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search
        if num == 0 or num == 1:
            return True
        lo = 0
        hi = num
        while hi > lo:
            mi = (hi - lo) // 2
            if num / mi == mi:
                return True
            elif num / mi > mi:
                lo = mi + 1
            else:
                hi = mi
        return False

'''
Runtime: 36 ms, faster than 74.99% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 14 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.
'''