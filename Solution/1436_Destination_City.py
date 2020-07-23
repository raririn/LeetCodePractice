class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        depart = set([path[0] for path in paths])
        dest = set([path[1] for path in paths])

        for i in depart:
            dest.discard(i)
        
        for i in dest:
            return i

'''
Runtime: 72 ms, faster than 26.45% of Python3 online submissions for Destination City.
Memory Usage: 13.8 MB, less than 66.24% of Python3 online submissions for Destination City.
'''