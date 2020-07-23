class Solution:
    def reformatDate(self, date: str) -> str:
        import re
        date = date.split()
        month_d = {"Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05", 
            "Jun": "06", 
            "Jul": "07", 
            "Aug": "08", 
            "Sep": "09", 
            "Oct": "10", 
            "Nov": "11", 
            "Dec": "12"}
        day = re.sub('\D+', '', date[0])
        if len(day) == 1:
            day = '0' + day
        return date[2] + '-' + month_d[date[1]] + '-' + day

'''
Runtime: 36 ms, faster than 70.56% of Python3 online submissions for Reformat Date.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reformat Date.
'''