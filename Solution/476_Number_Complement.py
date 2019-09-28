class Solution:
    def findComplement(self, num: int) -> int:
        ret = 0
        power = 0
        while num > 0:
            ret = ret + (not (num % 2)) * (2**power)
            num = num // 2
            power = power + 1
        return ret

# Better: find the bit length and xor it with 111..1

'''
Runtime: 40 ms, faster than 32.56% of Python3 online submissions for Number Complement.
Memory Usage: 13.7 MB, less than 10.00% of Python3 online submissions for Number Complement.
'''