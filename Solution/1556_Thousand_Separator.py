class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        L = len(n)
        if L <= 3:
            return n
        L = L % 3
        if L:
            res = [n[:L%3]]
            n = n[L%3:]
        else:
            res = []
        res += [n[i:i+3] for i in range(0, len(n), 3)]

        return '.'.join(res)

'''
Runtime: 32 ms, faster than 74.39% of Python3 online submissions for Thousand Separator.
Memory Usage: 13.8 MB, less than 50.93% of Python3 online submissions for Thousand Separator.
'''