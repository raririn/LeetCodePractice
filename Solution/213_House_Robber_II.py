class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob_first = nums[:-1]
        rob_last = nums[1:]

        @lru_cache(3)
        def dp_rob_first(i):
            if i < 0:
                return 0
            return max(dp_rob_first(i-2) + rob_first[i], dp_rob_first(i-1))

        @lru_cache(3)
        def dp_rob_last(i):
            if i < 0:
                return 0
            return max(dp_rob_last(i-2) + rob_last[i], dp_rob_last(i-1))
        
        return max(dp_rob_first(len(nums)-2), dp_rob_last(len(nums)-2))


'''
Runtime: 28 ms, faster than 89.62% of Python3 online submissions for House Robber II.
Memory Usage: 14 MB, less than 11.92% of Python3 online submissions for House Robber II.
'''