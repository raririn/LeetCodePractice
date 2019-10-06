class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        dd = [0] * len(T)
        dst = [0]
        for i in range(1, len(T)):
            if T[i] > T[i-1]:
                for j in range(len(dst)-1, -1, -1):
                    if T[dst[j]] < T[i]:
                        dd[dst[j]] = i - dst[j]
                        dst.pop()
                    else:
                        break
            dst.append(i)
        return dd

'''
Runtime: 560 ms, faster than 38.26% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.2 MB, less than 26.32% of Python3 online submissions for Daily Temperatures.
'''