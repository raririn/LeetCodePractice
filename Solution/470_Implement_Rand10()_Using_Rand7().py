# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b = rand7(), rand7()
        s = (a - 1) * 7 + b
        if s >= 41:
            return self.rand10()
        else:
            return s % 10 + 1