"""
Understand:
input = an array of integers
output = an integer
constraints = 1 <= heights.length <= 1000 and 0 <= heights[i] <= 1000
edge cases = an empty array

Plan:
1. Declare stack variable to store both index and variable
2. Loop with enumerate
3. When there is a bar lower than the previous bar, drop the previous bar and get the width
4. 

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                area = max(area, h * (i - index))
                start = index
            stack.append((start, height))

        for i, h in stack:
            area = max(area, h * (len(heights) - i)) 
        return area    




        