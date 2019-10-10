class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(tuple(map(len, ''.join(tuple(map(str, nums))).split('0'))))

'''
Runtime: 436 ms, faster than 23.33% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Max Consecutive Ones.
'''