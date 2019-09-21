class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = dict()
        for i in A:
            d[i] = d.get(i, 0) + 1
            if d[i] > 1:
                return i
        return False

'''
Runtime: 236 ms, faster than 88.38% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.1 MB, less than 6.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.
'''