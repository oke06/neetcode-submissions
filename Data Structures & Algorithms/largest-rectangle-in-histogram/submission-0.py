class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                largest = max(largest, area)
                start = index
            stack.append([start, h])

        for i, h in stack:
            area = h * (len(heights) - i)
            largest = max(area, largest)
        return largest
        
        