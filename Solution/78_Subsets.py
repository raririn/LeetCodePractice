class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        ret = [[]]
        for num in nums:
            ret += [i + [num] for i in ret]
        return ret

'''
Runtime: 36 ms, faster than 30.51% of Python3 online submissions for Subsets.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subsets.
'''