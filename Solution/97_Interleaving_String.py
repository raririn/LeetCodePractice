class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3
        if l3 != l1 + l2:
            return False
        dp = [[0] * l3 for _ in range(l3)]
        for i in range(0, l1+1):
            for j in range(0, l2+1):
                if (not i) and (not j):
                    dp[i][j] = True
                elif not i:
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[i+j-1])
                elif not j:
                    dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
                else:
                    dp[i][j] = (dp[i][j-1] and (s2[j-1] == s3[i+j-1])) or dp[i-1][j] and (s1[i-1] == s3[i+j-1])
        #print(dp)
        return dp[l1][l2]

'''
Runtime: 44 ms, faster than 62.44% of Python3 online submissions for Interleaving String.
Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Interleaving String.
'''