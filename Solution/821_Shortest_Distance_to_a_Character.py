class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        def isC(x, C):
            if x == C:
                return 0
            else:
                return 1
        ret = [(9999, 9999)] + [([isC(S[i], C)] * 2) for i in range(len(S))] + [(9999, 9999)]
        for i in range(1, len(ret)-1):
            if ret[i][0]:
                ret[i][0] = ret[i-1][0] + 1 
        for i in range(len(ret)-2, 0, -1):
            if ret[i][1]:
                ret[i][1] = ret[i+1][1] + 1
        ret = [min(i) for i in ret]
        ret.pop(0)
        ret.pop()
        return ret
    
'''
Runtime: 52 ms, faster than 53.19% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.1 MB, less than 7.69% of Python3 online submissions for Shortest Distance to a Character.
'''