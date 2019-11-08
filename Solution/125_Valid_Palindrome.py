class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = (re.sub("[^a-zA-Z0-9]+", "", s)).lower()
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

'''
Runtime: 40 ms, faster than 98.30% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14 MB, less than 52.38% of Python3 online submissions for Valid Palindrome.
'''