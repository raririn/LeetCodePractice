class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        heights.append(-1)
        peakIndex = []
        # Get every peak: if it is larger than its successor
        for i in range(len(heights)-1):
            if heights[i] > heights[i+1]:
                peakIndex.append(i)
        areaL = []
        # Iterate to calculate the maximum area for every peak (as right edge)
        for i in range(len(peakIndex)-1, -1, -1):
            curBuild = peakIndex[i]
            area = heights[curBuild]
            minHeight = heights[curBuild]
            for j in range(curBuild-1, -1, -1):
                if heights[j] < minHeight:
                    minHeight = heights[j]
                if (curBuild - j + 1) * minHeight > area:
                    area =  (curBuild - j + 1) * minHeight
            areaL.append(area)
        
        return max(areaL)
        
'''
Runtime: 144 ms, faster than 13.32% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 15.5 MB, less than 9.09% of Python3 online submissions for Largest Rectangle in Histogram.
'''