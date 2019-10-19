class Solution:
    def fib(self, N: int) -> int:
        fi = [0] * (N+1)
        fi[1] = 1
        for i in range(1, N+1):
            fi[i] = fi[i-1] + fi[i-2]
        return fi[-1]

'''
Runtime: 24 ms, faster than 99.76% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
'''