class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return [i[0] for i in sorted([[i, (i[0])**2 + (i[1])**2] for i in points], key = lambda x: x[1])[:K]]

'''
Runtime: 764 ms, faster than 62.18% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.3 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.
'''