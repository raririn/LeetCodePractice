class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        ptr = 0
        for i in range(c[0]):
            nums[ptr] = 0
            ptr+=1
        for i in range(c[1]):
            nums[ptr] = 1
            ptr+=1
        for i in range(c[2]):
            nums[ptr] = 2
            ptr+=1

'''
Runtime: 32 ms, faster than 60.64% of Python3 online submissions for Sort Colors.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Sort Colors.
'''