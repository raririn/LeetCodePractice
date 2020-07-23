class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxlen = len(max(words, key=len))

        ret_l = [[" "] * len(words) for _ in range(maxlen)]

        for idx, i in enumerate(words):
            for jdx, j in enumerate(i):
                ret_l[jdx][idx] = j
        
        return ["".join(i).rstrip() for i in ret_l]

'''
Runtime: 28 ms, faster than 81.60% of Python3 online submissions for Print Words Vertically.
Memory Usage: 13.8 MB, less than 66.22% of Python3 online submissions for Print Words Vertically.
'''