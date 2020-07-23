class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        ret = -1
        for k, v in c.items():
            if k == v:
                ret = max(ret, k)
        return ret

'''
Runtime: 52 ms, faster than 94.58% of Python3 online submissions for Find Lucky Integer in an Array.
Memory Usage: 13.7 MB, less than 85.71% of Python3 online submissions for Find Lucky Integer in an Array.
'''