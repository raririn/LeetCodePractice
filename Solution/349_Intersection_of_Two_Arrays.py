class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

'''
Runtime: 56 ms, faster than 61.31% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Intersection of Two Arrays.
'''