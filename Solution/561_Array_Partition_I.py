class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# Python list slicing
# https://stackoverflow.com/questions/509211/understanding-slice-notation

'''
Runtime: 336 ms, faster than 52.83% of Python3 online submissions for Array Partition I.
Memory Usage: 16.4 MB, less than 6.06% of Python3 online submissions for Array Partition I.
'''