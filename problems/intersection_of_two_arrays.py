def intersection(n2, n1):
    # length of n1 is less than or equal to n2
    dict1 = {}
    result = []
    for n in n1:
        if n in dict1:
            dict1[n] = dict1[n] + 1
        else:
            dict1[n] = 1
    for n in n2:
        if n in dict1:
            if dict1[n] > 0:
                result.append(n)
                dict1[n] = dict1[n] - 1
    return result


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        if len(nums1) == 0 or len(nums2) == 0:
            return result
        if len(nums1) < len(nums2):
            result = intersection(nums1, nums2)
        else:
            result = intersection(nums2, nums1)

        return result

