class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[0] = 1
        sumcount = 0
        ret = 0
        for num in nums:
            sumcount = sumcount + num
            ret = ret + d.get(sumcount - k, 0)
            d[sumcount] = d.get(sumcount, 0) + 1
        return ret

'''
Why not set or list? Consider [0, 0, 0]. There should be 3.
Runtime: 132 ms, faster than 56.07% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.4 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.
'''