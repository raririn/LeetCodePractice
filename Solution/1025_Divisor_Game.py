class Solution:
    def divisorGame(self, N: int) -> bool:
        if N % 2 == 0:
            return True
        else:
            return False

'''
A player starting with odd number can only choose odd number -> his opponent will always have even number -> he eventually gets 1 and loses
'''


'''
Runtime: 40 ms, faster than 48.98% of Python3 online submissions for Divisor Game.
Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Divisor Game.
'''