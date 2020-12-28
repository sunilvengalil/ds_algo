
NUM_SYMBOLS_LOWER_CASE_STRING = 26
FIRST_SYMBOLS_LOWER_CASE_STRING = 'a'
LAST_SYMBOLS_LOWER_CASE_STRING = 'z'


def atoi(ch) -> int:
    return ord(ch) - ord(FIRST_SYMBOLS_LOWER_CASE_STRING)


def get_char_count(s: str) -> str:
    if not s:
        return s
    char_count = [0] * NUM_SYMBOLS_LOWER_CASE_STRING
    distinct_chars = set()
    for ch in s:
        if char_count[atoi(ch)] == 0:
            distinct_chars.add(ch)
        char_count[atoi(ch)] += 1
    char_count_char = []
    for ch in distinct_chars:
        char_count_char.append([char_count[atoi(ch)], ch])
    char_count_char = sorted(char_count_char, reverse=True)

    return char_count_char


def put_next_char(char_count_char, _result):
    _result.append(char_count_char[0][1])
    char_count_char[0][0] -= 1

    if char_count_char[0][0] == 0:
        char_count_char = char_count_char[1:]
        return char_count_char

    # keep the array sorted char_count_char[1:] is sorted.
    # So insert char_count_char[0] at the right position
    k = char_count_char[0]
    char_count_char = char_count_char[1:]
    pos = 0
    while pos < len(char_count_char) and char_count_char[pos][0] >= k[0]:
        pos += 1
    char_count_char.insert(pos, k)

    if pos == len(char_count_char):
        char_count_char.append(k)
    return char_count_char


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return S
        if len(S) == 1:
            return S
        # Get a sorted list of tuples. Each tuples is in the form (char_count, char)
        char_count_char = get_char_count(S)

        # same character repeated len(S) time.
        if len(char_count_char) == 1:
            return ""

        # Start with the character that is most frequent
        result = []
        char_count_char = put_next_char(char_count_char, result)
        while len(char_count_char) > 0 and char_count_char[0][0] != 0:
            if result[-1] == char_count_char[0][1]:
                if len(char_count_char) >= 2:
                    most_frequent = char_count_char[0]
                    _char_count_char = put_next_char(char_count_char[1:], result)
                    _char_count_char.insert(0, most_frequent)
                    char_count_char = _char_count_char
                else:
                    return ""
            else:
                char_count_char = put_next_char(char_count_char, result)
        return ''.join(result)


result = Solution().reorganizeString("aaaabbbbbc")
print(result)
