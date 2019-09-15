class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        0-1 Knapsack.
        Let dp[i] denote that whether we can find a subset of nums whose sum
        equals to i.

        Consider:

        dp[x] =|| dp[x - i] ?

        The answer should be NO. There might be overlapping.

        Q: How to prevent overlapping? A: Use a top-to-bottom loop.
        '''

        numsum = sum(nums)
        if numsum % 2 == 1:
            return False
        target = numsum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for j in nums:
            for i in range(target, j-1, -1):
                dp[i] = dp[i] or dp[i - j]
                
        return dp[-1]


'''
Runtime: 688 ms, faster than 48.77% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 13.7 MB, less than 22.73% of Python3 online submissions for Partition Equal Subset Sum.
'''