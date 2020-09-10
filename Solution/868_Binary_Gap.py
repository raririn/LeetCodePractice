class Solution:
    def binaryGap(self, N: int) -> int:
        res = 0
        cur = 0
        for idx, i in enumerate(bin(N)):
            if i == '1':
                res = max(res, (not cur == 0) * (idx - cur)) 
                cur = idx
        return res

'''
Runtime: 24 ms, faster than 96.18% of Python3 online submissions for Binary Gap.
Memory Usage: 13.8 MB, less than 72.36% of Python3 online submissions for Binary Gap.
'''