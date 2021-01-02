import unittest
from problems.string_multiply import Solution


class TestMultiply(unittest.TestCase):
    def _test_multiply(self, num1, num2):
        alg_result = Solution().multiply(num1, num2)
        actual_result = str(int(num1) * int(num2))
        self.assertEqual(alg_result, actual_result)

    def test_multiply(self):
        self._test_multiply("3", "9")
        self._test_multiply("30", "9")
        self._test_multiply("3", "90")
        self._test_multiply("35", "99")
        self._test_multiply("3", "95")
        self._test_multiply("999", "9")
        self._test_multiply("999", "99")
        self._test_multiply("1000", "0")



