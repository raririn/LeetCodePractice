class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ret = []
        # Up
        for i in range(8):
            cord = [king[0], king[1] - i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break    
        # Down
        for i in range(8):
            cord = [king[0], king[1] + i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break  
        # Right        
        for i in range(8):
            cord = [king[0] + i, king[1]]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break          
        # Left
        for i in range(8):
            cord = [king[0] - i, king[1]]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break      
        # Right-up
        for i in range(8):
            cord = [king[0] + i, king[1] - i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break         
        # Left-up
        for i in range(8):
            cord = [king[0] - i, king[1] - i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break
        # Right-down
        for i in range(8):
            cord = [king[0] + i, king[1] + i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break
        # Left-down
        for i in range(8):
            cord = [king[0] - i, king[1] + i]
            if cord[0] > 7 or cord[1] < 0:
                break
            if cord in queens:
                ret.append(cord)
                break
        return ret

'''
Runtime: 48 ms, faster than 69.52% of Python3 online submissions for Queens That Can Attack the King.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Queens That Can Attack the King.
'''