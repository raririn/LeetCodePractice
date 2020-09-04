class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums), 2):
            output += [nums[i+1]] * nums[i]
        return output

'''
Runtime: 72 ms, faster than 67.17% of Python3 online submissions for Decompress Run-Length Encoded List.
Memory Usage: 14.1 MB, less than 47.70% of Python3 online submissions for Decompress Run-Length Encoded List.
'''