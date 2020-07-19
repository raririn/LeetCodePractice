class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in ((s+s)[1:2*len(s)-1])

'''
Runtime: 36 ms, faster than 81.50% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 13.8 MB, less than 80.74% of Python3 online submissions for Repeated Substring Pattern.
'''