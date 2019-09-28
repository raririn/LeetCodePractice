class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min([text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n')])

'''
Runtime: 40 ms, faster than 68.27% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
'''