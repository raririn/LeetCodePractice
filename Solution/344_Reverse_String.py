class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        r_list = []
        for i in range(len(s_list)):
            j = len(s_list) - i - 1
            r_list.append(s_list[j])
        r = ''.join(r_list)
        return r