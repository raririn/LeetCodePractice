class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        dp = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[-1]

'''
Runtime: 60 ms, faster than 95.05% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Min Cost Climbing Stairs.
'''