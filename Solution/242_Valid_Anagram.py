class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sum(list(map(lambda x:  (2**(ord(x)-96) + 105) % 131, tuple(s)))) == sum(list(map(lambda x:  (2**(ord(x)-96) + 105) % 131, tuple(t))))

'''
Runtime: 100 ms, faster than 5.08% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.8 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
'''