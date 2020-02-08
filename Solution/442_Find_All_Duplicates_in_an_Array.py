class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                ret.append(abs(i))
            nums[abs(i)-1] *= -1
        return ret

'''
Runtime: 404 ms, faster than 45.34% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 20.3 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.
'''