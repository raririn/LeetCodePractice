class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S) - 1:
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                if i != 0:
                    i = i - 1
            else:
                i = i + 1
        return S

'''
Runtime: 152 ms, faster than 13.34% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
'''