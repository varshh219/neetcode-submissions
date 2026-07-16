class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = i- index
                area = height * width
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, h))
        for index, height in stack:
            width = len(heights) - index
            area = height * width
            maxArea = max(maxArea, area)
        return maxArea

