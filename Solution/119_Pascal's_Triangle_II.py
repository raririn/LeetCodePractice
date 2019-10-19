from math import factorial
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def nCr(n, r):
            return factorial(n) // factorial(r) // factorial(n-r)
        return [nCr(rowIndex, i) for i in range(0, rowIndex + 1)]

'''
Runtime: 36 ms, faster than 77.49% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.
'''