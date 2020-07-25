NUM_SYMBOLS_LOWER_CASE_STRING = 26
FIRST_SYMBOLS_LOWER_CASE_STRING = 'a'


def atoi(ch)-> int:
    return ord(ch) - ord(FIRST_SYMBOLS_LOWER_CASE_STRING)


def sort_string_of_lower_case_alphabet(s: str) -> str:
    if not s:
        return s
    char_count = [0] * NUM_SYMBOLS_LOWER_CASE_STRING
    for ch in s:
        char_count[atoi(ch)] += 1

    # TODO can we do this in place?

    result = [''] * len(s)
    chars_index = 0

    for i in range(len(result)):
        while chars_index < len(char_count) and char_count[chars_index] == 0:
            chars_index += 1

        result[i] = chr( ord(FIRST_SYMBOLS_LOWER_CASE_STRING) + chars_index )
        char_count[chars_index] -= 1

    result_str = "".join(result)
    print(result_str)
    return result_str
