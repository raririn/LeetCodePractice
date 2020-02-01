class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        ret = 0
        flag = True
        for k, v in c.items():
            ret += (v // 2) * 2
            if flag and v % 2 == 1:
                ret += 1
                flag = False
        return ret


'''
Runtime: 28 ms, faster than 98.54% of Python3 online submissions for Longest Palindrome.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
'''