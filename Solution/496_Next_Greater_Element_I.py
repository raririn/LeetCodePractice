class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def retValue(num):
            for i in nums2[nums2.index(num):]:
                if i > num:
                    return i
            return -1
        return list(map(retValue, nums1))

'''
Runtime: 100 ms, faster than 16.54% of Python3 online submissions for Next Greater Element I.
Memory Usage: 14 MB, less than 7.41% of Python3 online submissions for Next Greater Element I.
'''