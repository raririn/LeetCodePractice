class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for idx, i in zip(index, nums):
            ret.insert(idx, i)
        return ret

'''
Runtime: 28 ms, faster than 93.27% of Python3 online submissions for Create Target Array in the Given Order.
Memory Usage: 14 MB, less than 11.76% of Python3 online submissions for Create Target Array in the Given Order.
'''