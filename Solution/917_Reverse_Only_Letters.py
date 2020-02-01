class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        S = [i for i in S]
        i, j = 0, len(S) - 1
        while i < j:
            if S[i].lower() in alpha and S[j].lower() in alpha:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            else:
                if not S[i].lower() in alpha:
                    i += 1
                if not S[j].lower() in alpha:
                    j -= 1
        return ''.join(S)

'''
Runtime: 24 ms, faster than 99.65% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.
'''