class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        left = 0
        right = n - 1
        
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            currArea = width * height
            maxArea = max(maxArea, currArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return maxArea