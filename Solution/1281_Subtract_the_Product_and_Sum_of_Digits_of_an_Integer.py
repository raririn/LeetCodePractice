class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        l = []
        while n > 0:
            l.append(n % 10)
            n = n // 10
        return reduce(lambda x, y: x*y, l) - sum(l)

'''
Runtime: 32 ms, faster than 18.41% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
'''