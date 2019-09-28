class Solution:
    def calPoints(self, ops: List[str]) -> int:
        validList = []
        validPtr = -1
        for i in ops:
            if i == "C":
                validList.pop()
                validPtr = validPtr - 1
            elif i == "D":
                validList.append(2*validList[-1])
                validPtr = validPtr + 1
            elif i == "+":
                validList.append(validList[-1] + validList[-2])
                validPtr = validPtr + 1
            else:
                validList.append(int(i))
                validPtr = validPtr + 1
        return sum(validList)

'''
Runtime: 52 ms, faster than 27.58% of Python3 online submissions for Baseball Game.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Baseball Game.
'''