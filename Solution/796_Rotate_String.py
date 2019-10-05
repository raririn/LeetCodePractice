class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A+A

# The idea is genius, I can't think of it.

'''
Runtime: 36 ms, faster than 67.68% of Python3 online submissions for Rotate String.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Rotate String.
'''
