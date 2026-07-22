class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i, h in enumerate(heights):
            for j in range(i+1, len(heights)):
                area = min(h, heights[j]) * (j - i)
                largest = max(largest, area)
        return largest
        