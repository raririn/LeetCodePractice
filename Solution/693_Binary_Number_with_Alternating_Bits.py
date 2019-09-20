class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n % 2 == 0:
            # It must be 1010...10
            a = 1
        else:
            # It must be 1010...101
            a = 0
        while n > 0:
            n = n - 2**a
            a = a + 2
        return n == 0

'''
Runtime: 32 ms, faster than 92.02% of Python3 online submissions for Binary Number with Alternating Bits.
Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Binary Number with Alternating Bits.
'''