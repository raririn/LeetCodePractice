class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        import math
        bin_x = []
        bin_y = []
        while x >= 1:
            bin_x.insert(0, x % 2)
            x = x // 2
        while y >= 1:
            bin_y.insert(0, y % 2)
            y = y // 2
        if len(bin_y) > len(bin_x):
            bin_s = bin_y
            bin_y = bin_x
            bin_x = bin_s
        if len(bin_x) > len(bin_y):
            while len(bin_x) > len(bin_y):
                bin_y.insert(0, 0)
        final_length = len(bin_x)
        hamming_distance = 0
        for i in range(final_length):
            if bin_x[i] != bin_y[i]:
                hamming_distance = hamming_distance + 1
        return hamming_distance
        #return bin_x, bin_y

# A naive solution with low running efficiency.
# 36ms
# Using XOR operation(^) might be more efficient.