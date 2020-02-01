"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        f = customfunction.f
        ret = []
        for x in range(1, 1001):
            if f(x, 1) > z:
                break
            for y in range(1, 1001):
                if f(x, y) == z:
                    ret.append([x, y])
                elif f(x, y) > z:
                    break
        return ret


'''
Runtime: 32 ms, faster than 98.41% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find Positive Integer Solution for a Given Equation.
'''