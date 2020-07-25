class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ret = start
        for i in range(1, n):
            ret = ret ^ (start+2*i)
        return ret

'''
Runtime: 48 ms, faster than 24.57% of Python3 online submissions for XOR Operation in an Array.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for XOR Operation in an Array.
'''