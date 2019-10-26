class Solution(object):
    def largestTriangleArea(self, points):
        def area(a, b, c):
            return 0.5 * abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[1]*b[0]-b[1]*c[0]-c[1]*a[0])
        return max(area(*tri) for tri in itertools.combinations(points, 3))

'''
Runtime: 164 ms, faster than 51.52% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Largest Triangle Area.
'''