class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(str1, str2):
            i = 0
            ret = ''
            while i < len(str1) and i < len(str2):
                if str1[i] == str2[i]:
                    ret += str1[i]
                    i += 1
                else:
                    break
            return ret
        
        if len(strs) == 0:
            return ''
        l = strs[0]
        for i in strs:
            l = lcp(l, i)
        return l

'''
Runtime: 40 ms, faster than 73.31% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
'''