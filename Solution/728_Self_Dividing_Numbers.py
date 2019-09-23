class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right + 1):
            isSDN = True
            store_i = i
            while i > 0 and isSDN:
                if i % 10 == 0:
                    isSDN = False
                else:
                    isSDN = isSDN and (store_i % (i % 10) == 0)
                i = i // 10
            if isSDN:
                ret.append(store_i)
        return ret


'''
Runtime: 60 ms, faster than 62.05% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 14 MB, less than 8.00% of Python3 online submissions for Self Dividing Numbers.
'''