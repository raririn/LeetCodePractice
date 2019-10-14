class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] > target:
                hi = mi
            elif nums[mi] < target:
                lo = mi + 1
            else:
                return mi
        return -1

'''
Runtime: 288 ms, faster than 61.79% of Python3 online submissions for Binary Search.
Memory Usage: 15.1 MB, less than 6.45% of Python3 online submissions for Binary Search.
'''