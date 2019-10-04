class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] == 2:
                return True
        return False

'''
Runtime: 136 ms, faster than 93.48% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.3 MB, less than 7.55% of Python3 online submissions for Contains Duplicate.
'''