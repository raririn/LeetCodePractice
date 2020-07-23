class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[0] for i in sorted([(idx, sum(i)) for idx, i in enumerate(mat)], key = lambda x: x[1])[:k]]

'''
Runtime: 120 ms, faster than 45.92% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 13.9 MB, less than 68.68% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''