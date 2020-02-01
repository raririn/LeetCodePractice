class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) <= 1:
            return set(name) == set(typed)
        i, j = 0, 0
        lastsync = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                lastsync = i
                i += 1
                j += 1
            else:
                if name[lastsync] == typed[j]:
                    j += 1
                else:
                    return False
        if i < len(name):
            return False
        for k in range(j, len(typed)):
            if typed[k] != name[-1]:
                return False
        return True


'''
Runtime: 32 ms, faster than 94.63% of Python3 online submissions for Long Pressed Name.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Long Pressed Name.
'''