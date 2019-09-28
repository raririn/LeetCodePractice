class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        ret = 0
        power = 0
        while N > 0:
            ret = ret + (not (N % 2)) * (2**power)
            N = N // 2
            power = power + 1
        return ret

# Same problem as 476

'''
Runtime: 36 ms, faster than 67.36% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Complement of Base 10 Integer.
'''