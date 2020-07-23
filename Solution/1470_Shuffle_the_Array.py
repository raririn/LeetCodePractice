class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i+n])
        return ret

'''
Runtime: 68 ms, faster than 54.27% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.
'''