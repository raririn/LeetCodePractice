class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calstep(diff: List[int]) -> int:
            x, y = diff[0], diff[1]
            return max(abs(x), abs(y))
        
        ret = 0
        for i in range(1, len(points)):
            last = points[i-1]
            cur = points[i]
            ret += calstep([cur[0]-last[0], cur[1]-last[1]])
        return ret

'''
Runtime: 60 ms, faster than 57.47% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
'''