class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        d1 = distance(p1, p2)
        d2 = distance(p1, p3)
        d3 = distance(p1, p4)
        d4 = distance(p2, p3)
        d5 = distance(p2, p4)
        d6 = distance(p3, p4)
        c = collections.Counter([d1, d2, d3, d4, d5, d6])
        f1, f2 = False, False
        for k, v in c.items():
            if v == 4:
                f1 = True
            if v == 2:
                f2 = True
        return (f1 and f2)

'''
Runtime: 40 ms, faster than 75.46% of Python3 online submissions for Valid Square.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Valid Square.
'''