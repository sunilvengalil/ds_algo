NUM_SYMBOLS_LOWER_CASE_STRING = 26
FIRST_SYMBOLS_LOWER_CASE_STRING = 'a'
LAST_SYMBOLS_LOWER_CASE_STRING = 'z'
from typing import List
"""
https://leetcode.com/problems/find-common-characters/
https://leetcode.com/problems/find-common-characters/submissions/

next 

https://leetcode.com/problems/word-ladder-ii/
https://leetcode.com/problems/contiguous-array/
"""


def atoi(ch) -> int:
    return ord(ch) - ord(FIRST_SYMBOLS_LOWER_CASE_STRING)


def itoa(i) -> str:
    return chr(i + ord(FIRST_SYMBOLS_LOWER_CASE_STRING))


def get_intersection(map_1, map_2):
    result = [0] * NUM_SYMBOLS_LOWER_CASE_STRING
    for i, count in enumerate(map_1):
        if count == 0:
            continue
        result[i] = min(map_2[i], count)
    return result


def get_char_count(s):
    result = [0] * NUM_SYMBOLS_LOWER_CASE_STRING
    for ch in s:
        result[atoi(ch)] += 1
    return result


def to_list(char_map):
    char_list = []
    for i, c in enumerate(char_map):
        if c > 0:
            char_list.extend(itoa(i) * c)
    return char_list


class Solution(object):

    def commonChars(self, A: List[str]) -> List[str]:
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 0:
            return []
        result_map = get_char_count(A[0])
        if len(A) == 1:
            return to_list(result_map)

        for a in A:
            char_map = get_char_count(a)
            result_map = get_intersection(result_map, char_map)
        return to_list(result_map)

result = Solution().commonChars(["aaaabbbbbc","abc"])
print(result)
