class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        pos = nums[-1] * nums[-2] * nums[-3]
        greedy = nums[0] * nums[-1] * nums[1]
        
        return max(pos, greedy)

'''
Runtime: 320 ms, faster than 56.61% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 15 MB, less than 6.67% of Python3 online submissions for Maximum Product of Three Numbers.
'''