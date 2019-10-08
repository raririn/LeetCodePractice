class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(1, 2*len(s)+2):
            if i % 2 == 1:
                left = (i-1)//2
                right = (i+1)//2
            else:
                ret = ret + 1
                left = i//2 - 1
                right = i//2 + 1
            while (left >= 0) and (right <= len(s)-1):
                if s[left] != s[right]:
                    break
                ret = ret + 1
                left = left - 1
                right = right + 1
        return ret

'''
Runtime: 148 ms, faster than 54.26% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Palindromic Substrings.
'''