class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for i in s + t:
            ret ^= ord(i)
        return chr(Ret)

'''
Runtime: 40 ms, faster than 75.50% of Python3 online submissions for Find the Difference.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Find the Difference.
'''