class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        saveDist = {}
        for i, num in enumerate(nums):
            if not num in saveDist:
                saveDist[target - num] = i
            else:
                return [i, saveDist[num]]