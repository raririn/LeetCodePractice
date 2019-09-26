class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month = month + 12
            year = year - 1
        c = year // 100
        y = year % 100
        return days[(y + y//4 + c//4 - 2*c + 26*(month+1)//10 + day - 1) % 7]


# https://en.wikipedia.org/wiki/Zeller%27s_congruence

'''
Runtime: 32 ms, faster than 90.03% of Python3 online submissions for Day of the Week.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Day of the Week.
'''