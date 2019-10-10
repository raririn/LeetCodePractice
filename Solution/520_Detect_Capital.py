class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        elif word[1:].islower() and wprd[0].isupper():
            return True
        else:
            return False

'''
Runtime: 40 ms, faster than 42.73% of Python3 online submissions for Detect Capital.
Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Detect Capital.
'''