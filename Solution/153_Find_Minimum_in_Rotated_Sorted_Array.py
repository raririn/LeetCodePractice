class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        slow = 0
        fast = 1
        while fast < len(nums) and nums[slow] < nums[fast]:
            slow += 1
            fast += 1
        if fast == len(nums):
            return nums[0]
        return nums[fast]


'''
Runtime: 48 ms, faster than 42.41% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14 MB, less than 67.86% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
'''