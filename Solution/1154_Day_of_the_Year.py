class Solution:
    def dayOfYear(self, date: str) -> int:
        import calendar
        date = date.split('-')
        y, m, d = int(date[0]), int(date[1]), int(date[2])
        if m <= 2:
            return d + 31 * (m == 2)
        ret = d + 31 + calendar.isleap(y)
        if m >= 3:
            ret += 28
        if m >= 4:
            ret += 31
        if m >= 5:
            ret += 30
        if m >= 6:
            ret += 31
        if m >= 7:
            ret += 30
        if m >= 8:
            ret += 31
        if m >= 9:
            ret += 31
        if m >= 10:
            ret += 30
        if m >= 11:
            ret += 31
        if m >= 12:
            ret += 30
        return ret

'''
Runtime: 28 ms, faster than 98.68% of Python3 online submissions for Day of the Year.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Day of the Year.
'''