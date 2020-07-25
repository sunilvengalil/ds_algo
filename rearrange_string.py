from copy import copy
from queue import PriorityQueue

NUM_SYMBOLS_LOWER_CASE_STRING = 26
FIRST_SYMBOLS_LOWER_CASE_STRING = 'a'
LAST_SYMBOLS_LOWER_CASE_STRING = 'z'


def atoi(ch) -> int:
    return ord(ch) - ord(FIRST_SYMBOLS_LOWER_CASE_STRING)


def sort_string_of_lower_case_alphabet(s: str) -> str:
    if not s:
        return s
    char_count = [0] * NUM_SYMBOLS_LOWER_CASE_STRING
    for ch in s:
        char_count[atoi(ch)] += 1
    result_char_count = copy(char_count)

    # TODO can we do this in place?
    result = [''] * len(s)
    chars_index = 0
    for i in range(len(result)):
        while chars_index < len(char_count) and char_count[chars_index] == 0:
            chars_index += 1
        result[i] = chr(ord(FIRST_SYMBOLS_LOWER_CASE_STRING) + chars_index)
        char_count[chars_index] -= 1

    result_str = "".join(result)
    return result_str, result_char_count


def get_most_frequent_character(char_count, char_index_from, char_index_to):
    most_frequent_char_count = char_count[char_index_from]
    most_frequent_char = char_index_from
    for i in range(char_index_from + 1, char_index_to):
        if char_count[i] > most_frequent_char_count:
            most_frequent_char_count = char_count[i]
            most_frequent_char = i

    return most_frequent_char_count, most_frequent_char
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return S

        sorted_S, char_count = sort_string_of_lower_case_alphabet(S)

        print(char_count)
        char_index_from = 0

        while char_index_from < len(char_count) and char_count[char_index_from] == 0:
            char_index_from += 1

        char_index_to = len(S)
        while char_index_to > 0 and char_count[char_index_to] == 0:
            char_index_to -= 1
        most_frequent_char_count, most_frequent_char = get_most_frequent_character(char_count,
                                                                                   char_index_from,
                                                                                   char_index_to,
                                                                                   )

        print(char_index_from, char_index_to, most_frequent_char_count, most_frequent_char)
        result = [''] * NUM_SYMBOLS_LOWER_CASE_STRING
        result[0] = chr(ord(FIRST_SYMBOLS_LOWER_CASE_STRING) + most_frequent_char)
        char_count[most_frequent_char] -= 1

        prev_char = result[0]
        for i in range(1, len(S)):
            current_char_count, current_char = get_most_frequent_character(char_count,char_index_from,char_index_to)
            is_prev_and_current_char_different = prev_char != current_char
            if is_prev_and_current_char_different:
                result[i] = chr(ord(FIRST_SYMBOLS_LOWER_CASE_STRING) + current_char)
                char_count[current_char] -= 1
            else:
                while char_index_from < len(char_count) and char_count[char_index_from] == 0:
                    char_index_from += 1
                if char_index_from == len(char_count):
                    return ""

            prev_char = result[i]
        return ''.join(result)


result = Solution().reorganizeString("aab")
