class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        for char in s:
            ret *= 26
            ret += (ord(char) - 64)
        return ret


'''
Runtime: 24 ms, faster than 94.12% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
'''