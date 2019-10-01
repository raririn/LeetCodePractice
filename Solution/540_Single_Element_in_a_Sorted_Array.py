class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Note: hi should be an even number, as len(nums) should be odd!
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            # e.g. [3,3,7,7,10,11,11]
            # mi = (0+6)/2 = 3
            # nums[mi] = 7
            mi = (lo + hi) // 2
            mi_t = mi
            if mi % 2 == 0:
                mi_t = mi + 1
            if nums[mi_t] == nums[mi_t-1]:
                # which means, mi is left of the single element!
                lo = mi + 1
            elif nums[mi_t] == nums[mi_t+1]:
                hi = mi
            else:
                return nums[mi]
        return nums[lo]

'''
Runtime: 100 ms, faster than 5.66% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.2 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.
'''