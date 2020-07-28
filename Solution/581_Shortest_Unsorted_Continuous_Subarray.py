class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        start, end = -1, -2
        flag = True
        for i in range(len(nums)):
            if nums[i] != s[i]:
                start = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != s[i]:
                end = i
                break
        return end-start+1


'''
Runtime: 484 ms, faster than 6.43% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 15 MB, less than 71.78% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
'''