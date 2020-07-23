class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def convertToBin(l):
            ret = 0
            for i in l:
                ret = 2*ret + i
            return ret
        def revert(i: int):
            if i == 0:
                return 1
            else:
                return 0
        
        cur = [0, 0, 0, 0, 0]
        d = {}
        d[convertToBin(cur)] = (-1, -1)
        for idx, i in enumerate(s):
            if 'aeiou'.find(i) == -1:
                pass
            else:
                cur['aeiou'.find(i)-1] = revert(cur['aeiou'.find(i)-1])
            binary = convertToBin(cur)
            if binary in d:
                d[binary] = (d[binary][0], idx)
            else:
                d[binary] = (idx, idx)
            
        ret = 0
        for _, v in d.items():
            # A little explaination:
            # Let's take a look at string "eleetminicoworoep"
            # if v[0] (start of substring) is vowel:
            #   then the length should be calculated without it
            # Why? Think about the string above. The maximum appears
            # at v[1] = 13 (r) and v[0] = 0 (e).
            # s[:13] has vowel parity of [0,1,0,0,0] (count(e)=3)
            # s[:1] has vowel parity of [0,1,0,0,0] (count(e)=1)
            # We DON'T want to take s[0] into the substring here! 
            if s[v[0]] in 'aeiou' or v[0] == -1:
                ret = max(ret, v[1] - v[0])
            else:
                ret = max(ret, v[1] - v[0]+1)
        return ret
        
'''
Runtime: 1132 ms, faster than 15.71% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 19.2 MB, less than 95.35% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
'''