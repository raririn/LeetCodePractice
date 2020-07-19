class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        def getRes(x, k):
            if x % k == 0:
                return 0
            else:
                return abs(k - (x % k))
        d = {}
        for i in arr:
            # e.g. i = 1, k = 5
            # Check if 4 in d
            # If 4 in d: d[4] = d[4] - 1
            if getRes(i, k) in d:
                d[getRes(i, k)] = d[getRes(i, k)] - 1
                if d[getRes(i, k)] == 0:
                    d.pop(getRes(i, k))
            # If not, increment d[1]
            else:
                d[i%k] = d.get(i%k, 0) + 1
        if len(d) >= 1:
            return False
        else:
            return True

'''
Runtime: 1016 ms, faster than 33.33% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
Memory Usage: 27.9 MB, less than 100.00% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
'''