class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        if not len(tmp):
            return 0
        else:
            return len(s.split()[-1])

'''
Runtime: 44 ms, faster than 9.55% of Python3 online submissions for Length of Last Word.
Memory Usage: 14 MB, less than 24.97% of Python3 online submissions for Length of Last Word.
'''