class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0
        for i in points:
            d = {}
            for j in points:
                distance = (i[0] - j[0])**2 + (i[1] - j[1])**2
                d[distance] = d.get(distance, 0) + 1
            for k, v in d.items():
                ret = ret + v * (v - 1)
        return ret

'''
Runtime: 1264 ms, faster than 53.97% of Python3 online submissions for Number of Boomerangs.
Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Number of Boomerangs.
'''