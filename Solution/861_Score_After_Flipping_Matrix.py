class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        ret = 0
        for c in range(C):
            col = 0
            for r in range(R):
                # Flip if the first number is 0
                col += A[r][c] ^ A[r][0]
            ret += max(col, R - col) * 2 ** (C-c-1)
        return ret

'''
Runtime: 48 ms, faster than 41.34% of Python3 online submissions for Score After Flipping Matrix.
Memory Usage: 13.8 MB, less than 71.93% of Python3 online submissions for Score After Flipping Matrix.
'''