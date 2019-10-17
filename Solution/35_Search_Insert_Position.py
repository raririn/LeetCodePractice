class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) //2
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1
        return lo

'''
Runtime: 60 ms, faster than 63.41% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.3 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
'''