class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: 
            return 0

        left = 0
        right = n - 1
        leftMax = height[left]
        rightMax = height[right]
        area = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]

        return area