class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c:
            return nums
        import itertools
        ret = [[0] * c for _ in range(r)]
        ptr = 0
        nums = tuple(itertools.chain(*nums))
        for i in range(r):
            for j in range(c):
                ret[i][j] = nums[ptr]
                ptr = ptr + 1
        return ret

'''
Runtime: 140 ms, faster than 11.59% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 15 MB, less than 5.55% of Python3 online submissions for Reshape the Matrix.
'''