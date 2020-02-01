class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret = 0
        count = 0
        for i in s:
            if i == 'L':
                count -= 1
            else:
                count += 1
            if count == 0:
                ret += 1
        return ret

'''
Runtime: 28 ms, faster than 98.07% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
'''