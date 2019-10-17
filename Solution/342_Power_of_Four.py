class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if num % 4 != 0:
                return False
            num = num // 4
        return num == 1

'''
Runtime: 28 ms, faster than 99.00% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for Power of Four.
'''