class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        L, W = len(M), len(M[0])
        N = [[0] * W for _ in M]

        for i in range(L):
            for j in range(W):
                q = 0
                for ii in (i-1, i, i+1):
                    for jj in (j-1, j, j+1):
                        if 0 <= ii < L and 0 <= jj < W:
                            N[i][j] += M[ii][jj]
                            q += 1
                N[i][j] = N[i][j] // q

        return N

'''
Runtime: 720 ms, faster than 73.11% of Python3 online submissions for Image Smoother.
Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Image Smoother.
'''