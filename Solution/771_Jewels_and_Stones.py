class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        J_list = list(J)
        S_list = list(S)
        for i in S_list:
            if i in J_list:
                count = count + 1
        return count


# The problem becomes quite easy using Python list() function. However, I think it
# necessary to practice using pointers using C for this one.
