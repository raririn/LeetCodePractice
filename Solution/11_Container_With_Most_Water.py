class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(a, b):
            return min(height[a], height[b]) * abs(a-b)
        a, b = 0, len(height) - 1
        maxarea = 0
        while a < b:
            maxarea = max(maxarea, area(a, b))
            if height[a] <= height[b]:
                a += 1
            else:
                b -= 1
        return maxarea

'''
Runtime: 160 ms, faster than 12.62% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.4 MB, less than 74.74% of Python3 online submissions for Container With Most Water.
'''