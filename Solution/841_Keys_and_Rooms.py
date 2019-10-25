class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        st = [0]
        while st:
            cur = st.pop()
            for neighbor in rooms[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    st.append(neighbor)
        return not False in visited

'''
Runtime: 88 ms, faster than 18.87% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.2 MB, less than 9.09% of Python3 online submissions for Keys and Rooms.
'''