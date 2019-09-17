class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        diff = max(A) - min(A)
        if K == 0:
            return diff
        return max(0, diff - 2*K)

'''
Runtime: 136 ms, faster than 64.66% of Python3 online submissions for Smallest Range I.
Memory Usage: 15 MB, less than 11.11% of Python3 online submissions for Smallest Range I.
'''