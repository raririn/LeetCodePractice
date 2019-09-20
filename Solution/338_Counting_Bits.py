class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        bits_list = [0] * (num + 1)
        powval = 1
        for i in range(1, num + 1):
            if i % 2 == 1:
                bits_list[i] = bits_list[i-1] + 1
            else:
                if powval * 2 == i:
                    powval = i
                    bits_list[i] = 1
                else:
                    bits_list[i] = bits_list[powval] + bits_list[i - powval]
        return bits_list

'''
Runtime: 84 ms, faster than 30.68% of Python online submissions for Counting Bits.
Memory Usage: 15.8 MB, less than 18.18% of Python online submissions for Counting Bits.
'''