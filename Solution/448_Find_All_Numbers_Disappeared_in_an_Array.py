class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        inNums = [0] * (len(nums)+1)
        for i in nums:
            inNums[i] = 1
        for i in range(len(nums)+1):
            if not inNums[i]:
                ret.append(i)
        return ret[1:]

'''
Runtime: 424 ms, faster than 50.75% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.4 MB, less than 17.86% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''