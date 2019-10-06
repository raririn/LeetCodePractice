class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        from collections import Counter
        d = Counter(nums)
        ret = 0
        for i in d:
            if k > 0:
                if i + k in d:
                    ret = ret + 1
            else:
                if d[i] >= 2:
                    ret = ret + 1
        return ret

'''
Runtime: 148 ms, faster than 61.25% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 15.1 MB, less than 64.52% of Python3 online submissions for K-diff Pairs in an Array.
'''