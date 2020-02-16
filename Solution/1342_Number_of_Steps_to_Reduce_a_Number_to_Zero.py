class Solution:
    def numberOfSteps (self, num: int) -> int:
        if not num:
            return 0
        if num & 1:
            return 1 + self.numberOfSteps(num - 1)
        else:
            return 1 + self.numberOfSteps(num>>1)

'''
Runtime: 52 ms, faster than 6.44% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''