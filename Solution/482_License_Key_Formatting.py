class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        size = len(S)
        if size % K == 0:
            chunk1 = K
        else:
            chunk1 = size % K
        ret = S[:chunk1]
        while chunk1 < size:
            ret = ret + '-' + S[chunk1:chunk1+K]
            chunk1 += K
        return ret

'''
Runtime: 88 ms, faster than 27.96% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.3 MB, less than 30.77% of Python3 online submissions for License Key Formatting.
'''