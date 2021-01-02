"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/339/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 0:
            digits[0] = digits[0] + 1
            return digits
        for pos in range(len(digits) - 1, -1, -1):
            plus_one = digits[pos] + 1
            if plus_one == 10:
                digits[pos] = plus_one - 10
            else:
                digits[pos] = plus_one
                break
        if plus_one == 10:
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([9, 9, 9]))
print(Solution().plusOne([9]))
print(Solution().plusOne([4, 3, 9, 9]))
print(Solution().plusOne([2, 0, 9]))
print(Solution().plusOne([0]))
