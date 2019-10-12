class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g, reverse = True)
        s = sorted(s, reverse = True)
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j = j + 1
            i = i + 1
        return j

'''
Runtime: 212 ms, faster than 21.24% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.4 MB, less than 14.29% of Python3 online submissions for Assign Cookies.
'''