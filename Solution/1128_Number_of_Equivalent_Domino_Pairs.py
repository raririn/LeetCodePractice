class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        unidom = [10*min(i[0], i[1])+max(i[0], i[1]) for i in dominoes]
        d = dict()
        for i in unidom:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        ret = 0
        for key, value in d.items():
            ret = ret + (value * (value - 1) // 2)
        return ret

'''
Runtime: 284 ms, faster than 43.79% of Python3 online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 23.6 MB, less than 100.00% of Python3 online submissions for Number of Equivalent Domino Pairs.
'''