class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        mapped = list(map(self.toKeyPoints, buildings))
        while len(mapped) > 1:
            mapped.append(self.mergeSkylines(mapped[0], mapped[1]))
            mapped.pop(0)
            mapped.pop(0)
        return mapped[0] # Remove the outer parentheses
    
    @staticmethod
    def toKeyPoints(building: List[int]) -> List[List[int]]:
        return [[building[0], building[2]], [building[1], 0]]
        
    @staticmethod
    def mergeSkylines(skyline_1: List[List[int]], skyline_2: List[List[int]]) -> List[List[int]]:
        h1 = 0
        h2 = 0
        ret = []
        ptr1 = 0
        ptr2 = 0
        temp_height = -1    # Record the last added height for removing redundency
        while ptr1 < len(skyline_1) and ptr2 < len(skyline_2):
            if (skyline_1[ptr1][0] < skyline_2[ptr2][0]) or ((skyline_1[ptr1][0] == skyline_2[ptr2][0]) and (skyline_1[ptr1][1] > skyline_2[ptr2][1])):
                h1 = skyline_1[ptr1][1]
                if max(h1, h2) != temp_height:  # If the point has the same height with the last added one, it shouldn't be added. 
                    ret.append([skyline_1[ptr1][0], max(h1, h2)])
                ptr1 = ptr1 + 1
            elif (skyline_1[ptr1][0] > skyline_2[ptr2][0]) or ((skyline_1[ptr1][0] == skyline_2[ptr2][0]) and (skyline_1[ptr1][1] < skyline_2[ptr2][1])):
                h2 = skyline_2[ptr2][1]
                if max(h1, h2) != temp_height:
                    ret.append([skyline_2[ptr2][0], max(h1, h2)])
                ptr2 = ptr2 + 1
            else:   # When x1 == x2 and y1 == y2: No need to update height but add it to the result
                ret.append(skyline_1[ptr1])
                ptr1 = ptr1 + 1
                ptr2 = ptr2 + 1
            temp_height = max(h1, h2)
        if ptr1 < len(skyline_1):
            for i in range(ptr1, len(skyline_1)):
                ret.append(skyline_1[i])
        if ptr2 < len(skyline_2):
            for i in range(ptr2, len(skyline_2)):
                ret.append(skyline_2[i])
        return ret

'''
Runtime: 188 ms, faster than 21.60% of Python3 online submissions for The Skyline Problem.
Memory Usage: 18.9 MB, less than 10.00% of Python3 online submissions for The Skyline Problem.
'''