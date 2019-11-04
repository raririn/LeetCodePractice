class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

'''
Runtime: 304 ms, faster than 46.35% of Python3 online submissions for Minimum Moves to Equal Array Elements.
Memory Usage: 14.9 MB, less than 12.50% of Python3 online submissions for Minimum Moves to Equal Array Elements.
'''