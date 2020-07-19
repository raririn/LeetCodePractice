class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur_point = (0, 0)
        visited = set()
        visited.add(cur_point)
        d = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for i in path:
            cur_point = (cur_point[0]+d[i][0], cur_point[1]+d[i][1])
            if cur_point in visited:
                return True
            else:
                visited.add(cur_point)
            #print(cur_point)
        return False


'''
Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Path Crossing.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Path Crossing.
'''