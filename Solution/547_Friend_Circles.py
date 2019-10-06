class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.M = M
        self.visited = [0] * len(M)
        ret = 0
        for i in range(len(M)):
            ret = ret + self.DFS(i)
        return ret

    def DFS(self, node):
        if self.visited[node]:
            return 0
        st = [node]
        while len(st) > 0:
            cur = st.pop()
            self.visited[cur] = 1
            localvisited = []
            for i in range(len(self.M)):
                if self.M[cur][i] and (not self.visited[i]):
                    st.append(i)
        return 1

'''
Runtime: 364 ms, faster than 8.19% of Python3 online submissions for Friend Circles.
Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Friend Circles.
'''