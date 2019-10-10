class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five = five + 1
            if i == 10:
                five = five - 1
                if five < 0:
                    return False
                ten = ten + 1
            if i == 20:
                if ten:
                    ten = ten - 1
                    five = five - 1
                    if five < 0:
                        return False
                else:
                    five = five - 3
                    if five < 0:
                        return False
        return True

'''
Runtime: 160 ms, faster than 86.49% of Python3 online submissions for Lemonade Change.
Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for Lemonade Change.
'''