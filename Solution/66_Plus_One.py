class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = len(digits) - 1
        while cur >= 0:
            digits[cur] += 1
            if digits[cur] == 10:
                digits[cur] = 0
                left = 1
                cur -= 1
            else:
                left = 0
                break
        if cur <= 0 and left:
            digits = [1] + digits
        return digits

'''
Runtime: 36 ms, faster than 86.69% of Python3 online submissions for Plus One.
Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Plus One.
'''