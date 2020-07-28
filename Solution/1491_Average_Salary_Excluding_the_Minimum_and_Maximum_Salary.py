class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)

'''
Runtime: 28 ms, faster than 90.72% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
'''