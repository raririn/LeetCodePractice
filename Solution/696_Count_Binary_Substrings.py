class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('10', '1 0').replace('01', '0 1').split(' ')))
        if len(s) <= 1:
            return 0
        ret = 0
        for i in range(1, len(s)):
            ret = ret + min(s[i-1], s[i])
        return ret

'''
Runtime: 132 ms, faster than 93.95% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 15.3 MB, less than 8.33% of Python3 online submissions for Count Binary Substrings.
'''