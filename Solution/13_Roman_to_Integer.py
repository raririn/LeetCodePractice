class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i in range(len(s)):
            slow, fast = s[i], s[i+1:i+2]
            if fast and d[slow] < d[fast]:
                ret -= d[slow]
            else:
                ret += d[slow]
        return ret

'''
Runtime: 40 ms, faster than 99.54% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
'''