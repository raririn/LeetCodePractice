class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x = x^abs(i)
        l = len(bin(x)[2:]) - 1
        y, z = 0, 0
        flag_y, flag_z = True, True
        for i in nums:
            if (abs(i) >> l) % 2:
                if i < 0:
                    flag_y = not flag_y
                y = y ^ abs(i)
            else:
                if i < 0:
                    flag_z = not flag_z
                z = z ^ abs(i)
        if not flag_y:
            y = -y
        if not flag_z:
            z = -z
        return [y, z]

'''
Runtime: 64 ms, faster than 96.35% of Python3 online submissions for Single Number III.
Memory Usage: 15.4 MB, less than 50.00% of Python3 online submissions for Single Number III.
'''