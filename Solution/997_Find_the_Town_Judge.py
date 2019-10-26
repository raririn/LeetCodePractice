class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N+1):
            if count[i] == N - 1:
                return i
        return -1

'''
Runtime: 852 ms, faster than 59.89% of Python3 online submissions for Find the Town Judge.
Memory Usage: 18.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
'''