class Solution:
    def addDigits(self, num: int) -> int:
        ret = 0
        for i in num:
            ret = ret + i
        return ret % 9 

'''
Runtime: 36 ms, faster than 85.38% of Python3 online submissions for Add Digits.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Add Digits.
'''