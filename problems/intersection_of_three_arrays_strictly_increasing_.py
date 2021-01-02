"""
https://leetcode.com/problems/intersection-of-three-sorted-arrays/submissions/

next
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
https://leetcode.com/problems/rabbits-in-forest/

"""



from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Initialize pointer to second and third array to 0
        pointer2 = 0
        pointer3 = 0

        if len(arr1) == 0 or len(arr2) == 0 or len(arr3) ==0:
            return []

        # Initialize result to an empty list
        result = []
        # Iterate over each element of arr1
        for e in arr1:
            # Check if e is present in arr2 and arr3
            # print("Next Iteration",pointer2, pointer3)
            if arr2[pointer2] == e and arr3[pointer3] == e:
                # e is present in all three. add it to result
                result.append(e)
                if pointer2 < len(arr2) - 1:
                    pointer2 = pointer2 + 1
                if pointer3 < len(arr3) - 1:
                    pointer3 = pointer3 + 1
            else:
                pointer2, pointer3 = self.update_pointer(arr2, arr3, e, pointer2, pointer3, result)
            #print(pointer2, pointer3)
        return result

    def update_pointer(self, arr2, arr3, e, pointer2, pointer3, result):
        # all three different, current arr2 element is less than e
        while pointer2 < len(arr2) - 1 and arr2[pointer2] < e:
            pointer2 = pointer2 + 1
        while pointer3 < len(arr3) - 1 and arr3[pointer3] < e:
            pointer3 = pointer3 + 1
        if arr2[pointer2] == e and arr3[pointer3] == e:
            result.append(e)
        return pointer2, pointer3


arr1 = [17,381, 193,281,421,523,596,1484,1803,1853,1863]
arr2 = [381,770,1100,1164,1211,1483,1486,1639,1908,1988]
arr3 = []

final_result = Solution().arraysIntersection(arr1, arr2, arr3)
print(final_result)
