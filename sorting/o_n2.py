from typing import List
# NUM_SYMBOLS_LOWER_CASE_STRING = 26
# FIRST_SYMBOLS_LOWER_CASE_STRING = 'a'
# LAST_SYMBOLS_LOWER_CASE_STRING = 'z'
#
# def atoi(ch) -> int:
#     return ord(ch) - ord(FIRST_SYMBOLS_LOWER_CASE_STRING)


""" Insert character ch into the sorted string at correct position so that the
resulting string is sorted"""


def insert_into_sorted_list(ch_list: List, ch) ->str:
    if not ch_list:
        return [ch]
    # insert  ch at the last position
    result = ch_list + [ch]
    index = len(result) -1
    while index > 0 and ch <= result[index]:
        result[index] = result[index - 1]
        index -= 1
    if index == 0:
        result[index] = ch
    else:
        result[index + 1] = ch
    return "".join(result)


def _insert_into_sorted_list(ch_list: List, sorted_upto) ->str:
    if not ch_list:
        return ch_list
    # insert  ch at the last position
    index = sorted_upto - 1
    ch = ch_list[sorted_upto]
    while index >= 0 and ch < ch_list[index]:
        ch_list[index+1] = ch_list[index]
        index -= 1
    ch_list[index + 1] = ch
    return ch_list


def sort_string_of_lower_case_alphabet(s: str) -> str:
    if not s:
        return s
    if len(s) == 1:
        return s
    result = list(s)
    sorted_upto = 1
    # Insert s[sorted_upto] at proper location
    while sorted_upto < len(result):
        _insert_into_sorted_list(result, sorted_upto)
        sorted_upto += 1
    # "ilnsu"
    return "".join(result)
