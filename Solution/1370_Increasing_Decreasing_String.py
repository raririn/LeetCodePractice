class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        ret = []

        get_smallest = True
        while d:
            chars = [k for k, _ in d.items()]
            if get_smallest:
                chars = sorted(chars)
            else:
                chars = sorted(chars, reverse=True)
            get_smallest = not get_smallest
            for char in chars:
                ret.append(char)
                d[char] -= 1
                if d[char] == 0:
                    del d[char]
        
        return ''.join(ret)

'''
Runtime: 72 ms, faster than 67.95% of Python3 online submissions for Increasing Decreasing String.
Memory Usage: 13.7 MB, less than 90.97% of Python3 online submissions for Increasing Decreasing String.
'''