from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n = len(matrix[0])
        heights = [0] * n

        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_area = 0
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    max_area = max(max_area, height * (i - index))
                    start = index
                stack.append((start, h))
            for i, h in stack:
                max_area = max(max_area, h * (len(heights) - i))
            return max_area

        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
