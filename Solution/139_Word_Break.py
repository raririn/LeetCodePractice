class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for idx in range(len(s)):
            for word in wordDict:
                if idx-len(word)+1 < 0:
                    continue
                if idx-len(word)+1 == 0 or dp[idx-len(word)]:
                    if s[idx-len(word)+1:idx+1] == word:
                        dp[idx] = True
        return dp[-1]

'''
Runtime: 64 ms, faster than 22.64% of Python3 online submissions for Word Break.
Memory Usage: 13.8 MB, less than 91.46% of Python3 online submissions for Word Break.
'''