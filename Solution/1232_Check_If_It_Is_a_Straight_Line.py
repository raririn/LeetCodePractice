class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        if x2 == x1:
            k = 0
        else:
            k = (y2-y1)/(x2-x1)
        b = y1-k*x1
        for i in coordinates:
            if i[1] != k*i[0] + b:
                return False
        return True

'''
Runtime: 68 ms, faster than 80.00% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Check If It Is a Straight Line.
'''