class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        horizon = moves.count("U") - moves.count("D")
        vertical = moves.count("L") - moves.count("R")
        if horizon == 0 and vertical == 0:
            return True
        return False

# F**king confusing and strange problem. I don't think it's a bit useful.