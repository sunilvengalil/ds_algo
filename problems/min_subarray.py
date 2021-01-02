# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # find the sum of all elements
        total = sum(nums)
        # if it is divisible by p return 0
        if total % p == 0:
            return 0
        quotient = total // p
        reminder = total % p
        for sub_array_length in range(1, len(nums)):
            for r in range(quotient+1):
                # see if its possible to find a subarray of length sub_array_length whose total sum is r*p + remainder

result = Solution().minSubarray([1, 2, 3], 2)
print(result)
