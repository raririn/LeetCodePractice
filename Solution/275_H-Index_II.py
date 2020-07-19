class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ret = 0
        L = len(citations)
        for idx, cit in enumerate(citations):
            ret = max(ret, min(L-idx, cit))
        return ret

# A better approach: use binary search

'''
Runtime: 180 ms, faster than 18.33% of Python3 online submissions for H-Index II.
Memory Usage: 20.4 MB, less than 35.41% of Python3 online submissions for H-Index II.
'''