class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        ret = 0
        for _, v in c.items():
            ret += v*(v-1)//2
        return ret

'''
Runtime: 48 ms, faster than 49.58% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
'''