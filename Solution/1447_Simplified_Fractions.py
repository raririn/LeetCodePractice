class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        from math import gcd
        ret = []
        for i in range(2, n+1):
            for j in range(i):
                if gcd(i, j) == 1:
                    ret.append(str(j)+"/"+str(i))
        return ret

'''
Runtime: 288 ms, faster than 39.50% of Python3 online submissions for Simplified Fractions.
Memory Usage: 13.8 MB, less than 96.43% of Python3 online submissions for Simplified Fractions.
'''