class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        d = {}
        maxlen = 0
        d[0] = -1
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if not count in d:
                d[count] = i
            if count in d:
                maxlen = max(i - d[count], maxlen)
        return maxlen

'''
Runtime: 1000 ms, faster than 51.55% of Python3 online submissions for Contiguous Array.
Memory Usage: 18.3 MB, less than 16.67% of Python3 online submissions for Contiguous Array.
'''