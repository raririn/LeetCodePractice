class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        cur = 1
        last = s[0]

        for i in s[1:]:
            if i == last:
                cur += 1
            else:
                last = i
                res = max(res, cur)
                cur = 1
        res = max(res, cur)
        return res

'''
Runtime: 44 ms, faster than 68.95% of Python3 online submissions for Consecutive Characters.
Memory Usage: 14 MB, less than 22.84% of Python3 online submissions for Consecutive Characters.
'''