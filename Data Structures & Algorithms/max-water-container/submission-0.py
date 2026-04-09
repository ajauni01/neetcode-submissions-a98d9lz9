"""
Understand:
input = An array of integers
output = Integer
Constraints = 2 <= height.length <= 1000 and 0 <= height[i] <= 100
edge cases = empty list of array

Plan:
1. Since, we need to return the maximum number of water, we need to find the
area (length and height) and multiply them.

"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0

        for l in range(n):
            for r in range(l+1, n):
                water = (r-l) * min(heights[r],heights[l])
                max_water = max(water, max_water)
        return max_water    

        