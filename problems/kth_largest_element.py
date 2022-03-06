"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/361/
"""
from random import randint
from typing import List


def find_kth_smallest(nums, left, right, k):
    if k < 1:
        raise ValueError("parameter k should be greater than or equal to 1")
    k = k - 1
    if left == right:
        return nums[left]
    _pivot_index = randint(left, right)
    print("pivot_index", _pivot_index)
    pivot_index = partition(nums, left, right, _pivot_index)
    while pivot_index != k:
        print("pivot_index", pivot_index)
        print(nums)
        if pivot_index > k:
            right = pivot_index - 1
            _pivot_index = randint(left, pivot_index - 1)
            pivot_index = partition(nums, left, pivot_index - 1, _pivot_index)
        elif pivot_index < k:
            left = pivot_index + 1
            _pivot_index = randint(pivot_index + 1, right)
            pivot_index = partition(nums, pivot_index + 1, right, _pivot_index)
        print("pivot_index", pivot_index)
        print(nums)

    return nums[pivot_index]


def partition(nums, left, right, pivot_index):
    if right == left:
        return left
    pivot = nums[pivot_index]
    lp = left
    rp = right
    while lp < rp:
        while lp < rp and nums[lp] <= pivot:
            lp += 1
        while rp > lp and nums[rp] > pivot:
            rp -= 1
        if lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
    return lp


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest = find_kth_smallest(nums, 0, len(nums) - 1, len(nums) - k + 1)
        return kth_largest


#print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
a = [3,2,1,5,6,4]
print(a)
print(Solution().findKthLargest(a, 2))
