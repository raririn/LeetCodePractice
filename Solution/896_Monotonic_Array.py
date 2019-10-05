class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = -1 # 0: incresing, 1: decresing
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if flag == 1:
                    return False
                flag = 0
            elif A[i] < A[i-1]:
                if flag == 0:
                    return False
                flag = 1
        return True

'''
Runtime: 580 ms, faster than 33.75% of Python3 online submissions for Monotonic Array.
Memory Usage: 19.6 MB, less than 5.26% of Python3 online submissions for Monotonic Array.
'''