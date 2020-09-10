class NumArray:

    def __init__(self, nums: List[int]):
        from functools import lru_cache
        self.nums = nums
    

    @lru_cache(None)
    def _get_rangesums(self, num: int) -> int:
        if num < 0 or num > len(self.nums) - 1:
            return 0
        if num == 0:
            return self.nums[0]
        else:
            return self._get_rangesums(num-1) + self.nums[num]
        

    def sumRange(self, i: int, j: int) -> int:
        return self._get_rangesums(j) - self._get_rangesums(i-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

'''
Runtime: 96 ms, faster than 59.45% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 27.8 MB, less than 5.03% of Python3 online submissions for Range Sum Query - Immutable.
'''