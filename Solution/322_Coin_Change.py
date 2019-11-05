class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mx = float('inf')
        dp = [0] + [mx] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i-coin] + 1, dp[i])
        if dp[-1] == mx:
            return -1
        else:
            return dp[-1]

'''
Runtime: 1208 ms, faster than 76.52% of Python3 online submissions for Coin Change.
Memory Usage: 14 MB, less than 30.56% of Python3 online submissions for Coin Change.
'''