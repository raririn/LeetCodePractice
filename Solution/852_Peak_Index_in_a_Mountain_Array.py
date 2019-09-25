class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mi = int((lo + hi) / 2)
            if A[mi] > A[mi - 1]:
                lo = mi
            if A[mi] > A[mi + 1]:
                hi = mi
        return lo

'''
Runtime: 88 ms, faster than 84.78% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.1 MB, less than 6.06% of Python3 online submissions for Peak Index in a Mountain Array.
'''