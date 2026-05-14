class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0;
        for i, h in enumerate(heights):
            for j, w in enumerate(heights):
                    water = min(h,w) * (i-j)
                    if water > maxWater:
                        maxWater = water
        return maxWater;