class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3]:
            return False
        return True

'''
Runtime: 36 ms, faster than 69.07% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Rectangle Overlap.
'''