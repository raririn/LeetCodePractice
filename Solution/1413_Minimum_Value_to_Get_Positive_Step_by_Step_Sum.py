class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningSum = [0] * len(nums)
        runningSum[0] = nums[0]
        for i in range(1, len(nums)):
            runningSum[i] = runningSum[i-1] + nums[i]
        return max(1 - min(runningSum), 1)

'''
Runtime: 52 ms, faster than 20.38% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 13.7 MB, less than 93.40% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
'''