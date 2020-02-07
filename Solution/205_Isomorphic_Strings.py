class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        aux1, aux2 = "", ""
        d = {}
        count = 1
        for i in s:
            if not i in d:
                d[i] = str(count)
                count += 1
            aux1 += d[i]
        d = {}
        count = 1
        for i in t:
            if not i in d:
                d[i] = str(count)
                count += 1
            aux2 += d[i]
        return aux1 == aux2

'''
Runtime: 40 ms, faster than 57.06% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Isomorphic Strings.
'''