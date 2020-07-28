class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for idx, i in enumerate(s):
            if c[i] == 1:
                return idx
        return -1

'''
Runtime: 88 ms, faster than 90.73% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.8 MB, less than 89.50% of Python3 online submissions for First Unique Character in a String.
'''