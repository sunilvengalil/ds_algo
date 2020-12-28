from typing import List


def intersection(n1, n2):
    return [x for x in n1 if x in n2]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        if len(nums1) == 0 or len(nums2) == 0:
            return result
        if len(nums1) < len(nums2):
            result = intersection(set(nums1), set(nums2))
        else:
            result = intersection(set(nums2), set(nums1))

        return result
