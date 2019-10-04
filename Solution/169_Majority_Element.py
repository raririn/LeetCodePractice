class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in nums:
            if d[i] > len(nums) // 2:
                return i

'''
Runtime: 216 ms, faster than 15.59% of Python3 online submissions for Majority Element.
Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.
'''