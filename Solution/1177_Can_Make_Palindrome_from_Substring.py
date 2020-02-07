class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        dp = []
        dp.append([0]*26)


        for i in range(1, len(s)+1):
            new = dp[-1][:] # Important: deep copy the array
            new[ord(s[i-1]) - ord('a')] += 1
            dp.append(new)
        
        ret = []

        for h, t, k in queries:
            cur_count = [dp[t+1][i] - dp[h][i] for i in range(26)]
            ret.append((sum([i % 2 for i in cur_count]) // 2) <= k)
            
        return ret

'''
Runtime: 2744 ms, faster than 5.91% of Python3 online submissions for Can Make Palindrome from Substring.
Memory Usage: 65.4 MB, less than 100.00% of Python3 online submissions for Can Make Palindrome from Substring.
'''