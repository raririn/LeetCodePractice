class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a*b < 0:
            if a > 0:
                a, b = b, a
            if self.getSum(~a, 1) == b:
                return 0
            if self.getSum(~a, 1) < b:
                -((-a) + (-b))
                return self.getSum(~self.getSum(self.getSum(~a, 1), self.getSum(~b, 1)), 1)
                
        while (b != 0):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

# https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution

'''
Runtime: 28 ms, faster than 98.54% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Sum of Two Integers.
'''