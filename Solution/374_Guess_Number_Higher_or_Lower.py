# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 0
        hi = n
        mi = (hi + lo) // 2
        while guess(mi)!= 0:
            mi = (hi + lo) // 2
            if guess(mi) == 1:
                lo = mi + 1
            else:
                hi = mi
        return mi

'''
Runtime: 12 ms, faster than 87.85% of Python online submissions for Guess Number Higher or Lower.
Memory Usage: 11.9 MB, less than 11.11% of Python online submissions for Guess Number Higher or Lower.
'''