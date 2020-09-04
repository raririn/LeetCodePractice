class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        R, C = [False] * n, [False] * m
        for r, c in indices:
            R[r] ^= True
            C[c] ^= True
        
        return (m-sum(C))*sum(R) + (n-sum(R))*sum(C)


'''
Runtime: 44 ms, faster than 85.14% of Python3 online submissions for Cells with Odd Values in a Matrix.
Memory Usage: 13.8 MB, less than 61.34% of Python3 online submissions for Cells with Odd Values in a Matrix.
'''