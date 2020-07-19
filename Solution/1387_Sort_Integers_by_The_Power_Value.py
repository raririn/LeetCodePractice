class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def pow(x):
            if x == 1:
                return 1
            if x % 2 == 0:
                return pow(x//2) + 1
            else:
                return pow(3*x+1) + 1
        
        L = list(range(lo, hi+1))
        L = sorted(L, key=pow)
        return L[k-1]

'''
Runtime: 1372 ms, faster than 9.66% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 13.9 MB, less than 67.73% of Python3 online submissions for Sort Integers by The Power Value.
'''