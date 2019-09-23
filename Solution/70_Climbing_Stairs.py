class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]
    

'''
Runtime: 40 ms, faster than 26.03% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
'''