class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if (x == 1 or x == 0):
            x, y = y, x
        if (x == 1 or x == 0):
            if x + y <= bound:
                return [x + y]
            else:
                return []
        i, j = 0, 0
        ret = []
        while x**i < bound:
            j = 0
            if y != 1 and y != 0:
                while x**i + y **j <= bound:
                    print(i, j)
                    ret.append(x**i + y **j)
                    j = j + 1
            else:
                ret.append(x**i+y)
            i = i + 1
        return set(ret)

'''
Runtime: 40 ms, faster than 54.97% of Python3 online submissions for Powerful Integers.
Memory Usage: 14 MB, less than 12.50% of Python3 online submissions for Powerful Integers.
'''