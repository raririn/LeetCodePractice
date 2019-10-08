class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sub = [i for i in nums]
        for i in range(len(nums)):
            try:
                nums[sub[i]] = -sub[sub[i]]-1
            except:
                continue
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i
        return len(nums)

'''
Runtime: 172 ms, faster than 21.62% of Python3 online submissions for Missing Number.
Memory Usage: 14.9 MB, less than 6.45% of Python3 online submissions for Missing Number.
'''