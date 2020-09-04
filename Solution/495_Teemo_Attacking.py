class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        ret = 0
        for i in range(len(timeSeries)-1):
            ret += min(duration, timeSeries[i+1] - timeSeries[i])
        
        return ret+duration

'''
Runtime: 372 ms, faster than 30.03% of Python3 online submissions for Teemo Attacking.
Memory Usage: 15.1 MB, less than 61.10% of Python3 online submissions for Teemo Attacking.
'''