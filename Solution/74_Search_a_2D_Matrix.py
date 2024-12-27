class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0])-1
        px, py = 0, n
        curr = matrix[px][py]
        if target == curr:
            return True
        while target != curr and px <= m and py >= 0:
            assert px <= m
            assert py >= 0
            curr = matrix[px][py]
            print("Current pos: {} {} / {}, {}".format(px, py, curr, curr == target))
            if target > curr:
                px += 1
            elif target < curr:
                py -= 1
            else:
                return True

        return False