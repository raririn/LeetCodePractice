class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i
        return xor

'''
Runtime: 104 ms, faster than 43.93% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 6.56% of Python3 online submissions for Single Number.
'''