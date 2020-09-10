class Solution:
    def baseNeg2(self, N: int) -> str:
        if not N:
            return "0"
        res = ""
        while N:
            res = str(N & 1) + res
            N = - (N >> 1)
        return res

'''
Runtime: 20 ms, faster than 99.51% of Python3 online submissions for Convert to Base -2.
Memory Usage: 13.7 MB, less than 83.82% of Python3 online submissions for Convert to Base -2.
'''