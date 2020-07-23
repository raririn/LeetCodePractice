class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ret = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ret += 1
        return ret


'''
Runtime: 56 ms, faster than 19.32% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
Memory Usage: 13.8 MB, less than 71.43% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
'''