class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'
        chars = '0123456789abcdef'
        ret = ''
        for _ in range(8):
            ret = chars[num & 15] + ret
            num = num >> 4
            if not num:
                break
        return ret

'''
Runtime: 52 ms, faster than 5.44% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Convert a Number to Hexadecimal.
'''