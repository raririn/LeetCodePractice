class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return S
        ret = []
        def dfs(s, cur, ret):
            if len(s) == len(S):
                ret.append(s)
                return
            for i in range(cur, len(S)):
                if S[i].isalpha():
                    dfs(s + S[i].lower(), i+1, ret)
                    dfs(s + S[i].upper(), i+1, ret)
                else:
                    dfs(s + S[i], i+1, ret)
        dfs('', 0, ret)
        return ret

'''
Runtime: 1344 ms, faster than 5.06% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 14.2 MB, less than 20.00% of Python3 online submissions for Letter Case Permutation.
'''