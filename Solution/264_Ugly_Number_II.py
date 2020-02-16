class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ret = [1]
        ptr_2, ptr_3, ptr_5 = 0, 0, 0
        count = 1
        while count < n:
            new = min(ret[ptr_2]*2, ret[ptr_3]*3, ret[ptr_5]*5)
            if new != ret[-1]:
                ret.append(new)
                count += 1
            if new == ret[ptr_2] * 2:
                ptr_2 += 1
            elif new == ret[ptr_3] * 3:
                ptr_3 += 1
            else:
                ptr_5 += 1
        return ret[-1]


'''
Runtime: 668 ms, faster than 8.78% of Python3 online submissions for Ugly Number II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Ugly Number II.
'''