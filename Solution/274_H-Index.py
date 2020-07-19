class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        ret = 0
        L = len(citations)
        for idx, cit in enumerate(citations):
            ret = max(ret, min(L-idx, cit))
        return ret
    

'''
Runtime: 36 ms, faster than 69.94% of Python3 online submissions for H-Index.
Memory Usage: 14 MB, less than 57.48% of Python3 online submissions for H-Index.
'''