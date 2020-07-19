class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
        dp = [[[0] *(N) for _ in range(N)] for _ in range(K+1)]

        dp[0][r][c] = 1

        for i in range(K):
            for r, row in enumerate(dp[i]):
                for c, val in enumerate(row):
                    for move in moves:
                        if 0 <= r + move[0] < N and 0 <= c + move[1] < N:
                            dp[i+1][r+move[0]][c+move[1]] += val / 8.0
        ret = 0
        for i in range(N):
            for j in range(N):
                ret += dp[K][i][j]
                
        return ret

'''
Runtime: 404 ms, faster than 12.39% of Python3 online submissions for Knight Probability in Chessboard.
Memory Usage: 15.3 MB, less than 42.82% of Python3 online submissions for Knight Probability in Chessboard.
'''