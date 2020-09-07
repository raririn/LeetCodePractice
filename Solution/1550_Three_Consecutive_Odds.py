class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = 0
        for i in arr:
            if i & 1 == 1:
                flag += 1
                if flag == 3:
                    return True
            else:
                flag = 0
        return False

'''
Runtime: 52 ms, faster than 56.14% of Python3 online submissions for Three Consecutive Odds.
Memory Usage: 13.8 MB, less than 89.68% of Python3 online submissions for Three Consecutive Odds.
'''