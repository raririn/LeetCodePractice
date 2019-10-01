class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

'''
Runtime: 236 ms, faster than 70.39% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.1 MB, less than 12.50% of Python3 online submissions for Largest Perimeter Triangle.
'''