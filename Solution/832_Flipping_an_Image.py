class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ret = [[0] * len(A[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ret[i][j] = self.flipBool(A[i][len(A[0])-j-1])
        return ret
    
    @staticmethod
    def flipBool(x: int) -> int:
        if x:
            return 0
        else:
            return 1

# https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value

'''
Runtime: 60 ms, faster than 72.18% of Python3 online submissions for Flipping an Image.
Memory Usage: 14 MB, less than 6.00% of Python3 online submissions for Flipping an Image.
'''