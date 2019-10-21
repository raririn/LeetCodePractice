class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ret = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        while i < m:
            ret.append(nums1[i])
            i += 1
        while j < n:
            ret.append(nums2[j])
            j += 1
        for i in range(len(ret)):
            nums1[i] = ret[i]

'''
Runtime: 44 ms, faster than 72.62% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.
'''