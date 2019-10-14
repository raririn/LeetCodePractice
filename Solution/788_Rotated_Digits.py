class Solution:
    def rotatedDigits(self, N: int) -> int:
        s1 = set(['0', '1', '8'])
        s2 = s1 | set(['2', '5', '6', '9'])
        ret = 0
        for i in range(1, N+1):
            s = set([j for j in str(i)])
            if s.issubset(s2) and not s.issubset(s1):
                ret = ret + 1
        return ret

'''
Runtime: 132 ms, faster than 34.18% of Python3 online submissions for Rotated Digits.
Memory Usage: 13.7 MB, less than 50.00% of Python3 online submissions for Rotated Digits.
'''