class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
        '''
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)


'''
Runtime: 68 ms, faster than 98.47% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''