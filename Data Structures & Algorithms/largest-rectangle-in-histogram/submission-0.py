class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for idx, ht in enumerate(heights):
            popIdx, popHt = None, None
            while stack and stack[-1][1] > ht:
                popIdx, popHt = stack.pop()
                area = (idx - popIdx) * popHt
                maxArea = max(maxArea, area)
            stack.append((popIdx if popIdx is not None else idx, ht))

        wid = len(heights)
        for idx, ht in stack:
            area = (wid - idx) * ht
            maxArea = max(maxArea, area)
        return maxArea