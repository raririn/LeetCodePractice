class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        points = sorted(startTime + endTime)
        d = dict.fromkeys(points)
        points = tuple(d)
        #points = sorted(list(dict.fromkeys(startTime + endTime)))
        for index, point in enumerate(points):
        jobs = [[d[startTime[i]], d[endTime[i]], d[profit[i]]] for i in range(len(profit))]
        L = len(points)
        dp = [[0] * L for _ in range(L)]
        for i in jobs:
            p1 = i[0]
            p2 = i[1]
            dp[p1][p2] = i[2]
        for gap in range(1, L):
            for i in range(L):
                j = i + gap
                if j > L - 1:
                    continue
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])
                    #print(p1, p2, dp[p1][p2], dp[p1][pk], dp[pk][p2])
            
        #print(dp)
        return dp[0][-1]