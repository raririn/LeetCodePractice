class Solution:
    def reverseWords(self, s: str) -> str:
        def flip(s: str):
            r = ''
            for i in s:
                r = i + r
            return r
        return ' '.join(list(map(flip, s.split(' '))))

'''
Runtime: 64 ms, faster than 22.17% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''