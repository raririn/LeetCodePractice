class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1] * i for i in range(1, numRows+1)]
        for i in range(numRows):
            for j in range(1, i):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        return ret

'''
Runtime: 36 ms, faster than 75.65% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.
'''