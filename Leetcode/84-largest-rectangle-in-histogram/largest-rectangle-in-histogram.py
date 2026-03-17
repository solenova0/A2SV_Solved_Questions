class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))