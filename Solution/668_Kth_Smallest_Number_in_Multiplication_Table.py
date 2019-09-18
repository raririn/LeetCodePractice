class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def isLargerThanKNumbers(x: int, k: int):
            # For every column: it's 1*n ~ m*n
            return sum([min(x // i, n) for i in range(1, m + 1)]) >= k
        lo = 1
        hi = m*n
        while (lo < hi):
            mi = (lo + hi) // 2
            if isLargerThanKNumbers(mi, k):
                hi = mi
            else:
                lo = mi + 1
        return lo

'''
Runtime: 784 ms, faster than 66.67% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
Memory Usage: 14.8 MB, less than 50.00% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
'''