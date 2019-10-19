class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return len(s.split())

'''
Runtime: 28 ms, faster than 97.46% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.
'''