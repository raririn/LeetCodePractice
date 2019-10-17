class Solution:
    def isUgly(self, num: int) -> bool:
        if num != int(num) or num == 0:
            return False
        else:
            num = int(num)
        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        return self.isUgly(num / 2) or self.isUgly(num / 3) or self.isUgly(num / 5)

'''
Runtime: 40 ms, faster than 55.87% of Python3 online submissions for Ugly Number.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Ugly Number.
'''