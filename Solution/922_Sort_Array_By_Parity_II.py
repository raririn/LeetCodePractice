class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ret = [0] * len(A)
        pos_e = 0
        pos_o = 1
        for i in A:
            if i % 2 == 0:
                ret[pos_e] = i
                pos_e += 2
            else:
                ret[pos_o] = i
                pos_o += 2
        return ret

'''
Runtime: 244 ms, faster than 81.55% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16 MB, less than 8.70% of Python3 online submissions for Sort Array By Parity II.
'''