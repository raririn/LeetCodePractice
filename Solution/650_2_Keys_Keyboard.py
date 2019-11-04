class Solution:
    def minSteps(self, n: int) -> int:
        ret = 0
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                ret += divisor
                n /= divisor
            divisor += 1
        return ret

'''
Runtime: 36 ms, faster than 86.80% of Python3 online submissions for 2 Keys Keyboard.
Memory Usage: 13.7 MB, less than 8.33% of Python3 online submissions for 2 Keys Keyboard.
'''