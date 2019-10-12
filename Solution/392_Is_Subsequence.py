class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i + 1
            j = j + 1
        if i == len(s):
            return True
        else:
            return False
    
'''
Runtime: 280 ms, faster than 20.15% of Python3 online submissions for Is Subsequence.
Memory Usage: 18.4 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
'''