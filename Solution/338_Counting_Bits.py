class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits_list = []
        for i in range(num + 1):
            bits = 0
            while i >= 1:
                if i % 2 == 1:
                    bits = bits + 1
                i = i // 2
            bits_list.append(bits)
        return bits_list