class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            ret = ret + (n % 2)
            n = n >> 1
        return ret


'''
Runtime: 20 ms, faster than 49.70% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 52.50% of Python online submissions for Number of 1 Bits.
'''