class Solution:
    def numSteps(self, s: str) -> int:
        def bin2Dem(s: str):
            ret = 0
            for i in list(map(int, s)):
                ret *= 2
                ret += i
            return ret
        
        dem = bin2Dem(s)
        count = 0
        while dem != 1:
            if dem % 2:
                dem += 1
            else:
                dem = dem // 2
            count += 1
        return count

'''
Runtime: 48 ms, faster than 27.27% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
Memory Usage: 13.8 MB, less than 63.42% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
'''