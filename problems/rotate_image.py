"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3052/
"""
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for top_left_corner in range(n // 2):
            top = top_left_corner
            left = top_left_corner
            bottom = n - 1 - top
            right = n - 1 - left
            for c in range(right - left):
                # print("top_left_corner", top_left_corner)
                temp = matrix[top][c + left]
                matrix[top][c + left] = matrix[bottom-c][left]
                matrix[bottom-c][left] = matrix[bottom][right-c]
                matrix[bottom][right-c] = matrix[c + top][right]
                matrix[c + top][right] = temp


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]
          ]
print(matrix)
Solution().rotate(matrix)
print(matrix)
