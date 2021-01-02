import unittest
from problems.rotate_image import Solution
class TestRotateImage(unittest.TestCase):
    def test_rotate_image(self):
        matrix =[[1,2,3],[4,5,6],[7,8,9]]
        actual = [[7,4,1],[8,5,2],[9,6,3]]
        rotated = Solution().rotate(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.assertEqual(rotated[i][j],actual[i][j])