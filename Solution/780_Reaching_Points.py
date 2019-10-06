class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False

        # tx <= ty
        if tx > sx and ty == sy and (tx-sx)%sy==0:
            return True
        if ty > sy and (ty-sy)%sx==0 and tx == sx:
            return True
        
        return self.reachingPoints(sx, sy, tx%ty, ty%tx)

'''
Runtime: 36 ms, faster than 76.57% of Python3 online submissions for Reaching Points.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Reaching Points.
'''