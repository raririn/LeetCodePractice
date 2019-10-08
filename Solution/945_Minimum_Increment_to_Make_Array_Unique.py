class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(float('inf'))
        ret = 0
        dup = 0
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                dup = dup + 1
                ret = ret - A[i]
            elif A[i] - A[i-1] > 1:
                move = min(dup, A[i] - A[i-1] - 1)
                dup = dup - move
                ret = ret + move * (move+1) // 2 + A[i-1] * move
        return ret

'''
Runtime: 384 ms, faster than 73.68% of Python3 online submissions for Minimum Increment to Make Array Unique.
Memory Usage: 19.2 MB, less than 50.00% of Python3 online submissions for Minimum Increment to Make Array Unique.
'''