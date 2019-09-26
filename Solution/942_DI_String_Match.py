class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        pos = 0
        neg = 0
        ret = [0]
        for i in S:
            if i == "I":
                pos = pos + 1
                ret.append(pos)
            else:
                neg = neg - 1
                ret.append(neg)
        return [i - neg for i in ret]

'''
Runtime: 80 ms, faster than 44.23% of Python3 online submissions for DI String Match.
Memory Usage: 15 MB, less than 5.00% of Python3 online submissions for DI String Match.
'''