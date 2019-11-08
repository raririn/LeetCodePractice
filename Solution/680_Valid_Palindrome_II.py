class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.helper(s[i:j]) or self.helper(s[i+1:j+1])
        return True
        
    def helper(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

'''
Runtime: 168 ms, faster than 54.83% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 13.2 MB, less than 75.00% of Python3 online submissions for Valid Palindrome II.
'''