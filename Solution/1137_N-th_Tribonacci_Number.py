class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n <= 2:
            return arr[n]
        for i in range(3, n+1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[-1]

'''
Runtime: 40 ms, faster than 25.54% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.
'''