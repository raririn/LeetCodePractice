class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points[0], points[1], points[2]
        if p1 == p2 or p1 == p3 or p2 == p3:
            return False
        if p1[0] == p2[0] or p1[0] == p3[0] or p2[0] == p3[0]:
            if p1[0] == p2[0] == p3[0]:
                return False
            else:
                return True
        if (p1[1]-p2[1])/(p1[0]-p2[0]) == (p3[1]-p2[1])/(p3[0]-p2[0]):
            return False
        return True

'''
Runtime: 32 ms, faster than 96.45% of Python3 online submissions for Valid Boomerang.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Valid Boomerang.
'''