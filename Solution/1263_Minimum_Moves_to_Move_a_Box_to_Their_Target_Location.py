class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])

        def isOnGrid(t) -> bool:
            r, c = t
            if r < 0 or r >= self.R:
                return False
            if c < 0 or c >= self.C:
                return False
            if self.grid[r][c] == '#':
                return False
            return True

        def getNeighbors(t) -> List[int]:
            r, c = t
            return list(filter(isOnGrid, [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]))

        # Return if there is a path from start to goal
        def dfs(start, goal) -> bool:
            visited = set([start])
            stack = getNeighbors(start)
            while stack:
                cur = stack.pop()
                for i in getNeighbors(cur):
                    if i == goal:
                        return True
                    else:
                        stack.append(i)
            return False

        def heuristic(start, goal) -> int:
            return abs(start[0]-goal[0]) + abs(start[1]-goal[1])
        

        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == "T":
                    target = (r, c)
                elif grid[r][c] == "B":
                    box = (r, c)
                elif grid[r][c] == "S":
                    person = (r, c)
        
        # Format: (h(box_cur), moves, person_cur, box_cur)
        # Notice: heapq takes the first element as priority
        heap = [[heuristic(box, target), 0, person, box]]
        visited = set()

        while heap:
            h, moves, person_cur, box_cur = heapq.heappop(heap)
            if box_cur == target:
                return moves
            if (person_cur, box_cur) in visited:
                continue
            else:
                visited.add((person_cur, box_cur))

            for neighbor in getNeighbors(person_cur):
                # Only if the person moves to the position of the box can he push it
                if neighbor == box_cur:
                    dr, dc = neighbor[0]-person_cur[0], neighbor[1]-person_cur[1]
                    box_new = (box_cur[0]+dr, box_cur[1]+dc)
                    if not isOnGrid(box_new):
                        continue
                    heapq.heappush(heap, [heuristic(box_new, target)+moves+1, moves+1, neighbor, box_new])
                else:
                    heapq.heappush(heap, [heuristic(box_cur, target)+moves, moves, neighbor, box_cur])
        return -1
                

'''
Runtime: 1056 ms, faster than 14.00% of Python3 online submissions for Minimum Moves to Move a Box to Their Target Location.
Memory Usage: 21.6 MB, less than 16.67% of Python3 online submissions for Minimum Moves to Move a Box to Their Target Location.
'''