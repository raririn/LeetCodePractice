class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        front_ptr = 0
        back_ptr = len(A) - 1
        ret_ptr = len(A) - 1
        ret = [None] * len(A)
        while front_ptr <= back_ptr:
            if self.sq(A[front_ptr]) > self.sq(A[back_ptr]):
                ret[ret_ptr] = self.sq(A[front_ptr])
                front_ptr += 1
            else:
                ret[ret_ptr] = self.sq(A[back_ptr])
                back_ptr -= 1
            ret_ptr -= 1
        return ret

    @staticmethod
    def sq(x):
        return x*x