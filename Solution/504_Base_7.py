class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ret = ''
        if num > 0:
            flag = 1
        else:
            flag = 0
        num = abs(num)
        while num:
            ret = str(num%7) + ret
            num = num // 7
        if flag:
            return ret
        else:
            return '-' + ret

'''
Runtime: 48 ms, faster than 5.45% of Python3 online submissions for Base 7.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Base 7.
'''