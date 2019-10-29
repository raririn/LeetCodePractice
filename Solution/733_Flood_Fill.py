class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def getneighbor(x, y):
            n = []
            if x > 0:
                n.append((x-1, y))
            if y > 0:
                n.append((x, y-1))
            if x < len(image) - 1:
                n.append((x+1, y))
            if y < len(image[0]) - 1:
                n.append((x, y+1))
            return n
        st = [(sr, sc)]
        startColor = image[sr][sc]
        image[sr][sc] = newColor
        while st:
            cur = st.pop()
            for i in getneighbor(*cur):
                if image[i[0]][i[1]] == startColor and image[i[0]][i[1]] != newColor:
                    image[i[0]][i[1]] = newColor
                    st.append((i[0], i[1]))
        return image


'''
Runtime: 88 ms, faster than 87.25% of Python3 online submissions for Flood Fill.
Memory Usage: 13.7 MB, less than 5.56% of Python3 online submissions for Flood Fill.
'''