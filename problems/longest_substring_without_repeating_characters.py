class Solution:

    class Solution:
        def length_of_longest_substring_working(self, s: str) -> int:
            if len(s) <= 1:
                return len(s)

            substring = ""
            # Initialize Loop invariants - outer while loop
            # 1. Longest substring without repeating characters - s[current_start_index + 1: current_end_index]
            current_end_index = len(s)
            current_start_index = current_end_index - 1
            # Largest length  discovered so far
            max_length = 0

            # Initialize Loop invariants - inner while loop
            # 1. staring character of substring - ch
            ch = s[current_start_index]
            characters = set()
            #       substring = s[current_start_index:current_start_index]
            num_iter = 0
            print("num_iter\tcurrent_start_index\tcurrent_end_index\tch\tcharacters\tmax_length\tsubstring")
            while current_end_index > 0 and current_start_index > -1:
                print(
                    f"{num_iter}\t\t{current_start_index}\t\t\t{current_end_index}\t\t\t{ch}\t{characters}\t\t{max_length}\t\t{substring}")
                # Decrease the start index untill the first repeating character
                while current_start_index >= 0 and ch not in characters:
                    characters.add(ch)
                    current_start_index -= 1
                    ch = s[current_start_index]

                if current_start_index == -1:
                    return max(current_end_index + 1, max_length)

                max_substring = (current_start_index + 1, current_end_index)
                #           substring = s[current_start_index:current_end_index]
                cur_len = current_end_index - current_start_index - 1
                max_length = max(max_length, cur_len)
                print(
                    f"{num_iter}\t\t{current_start_index}\t\t\t{current_end_index}\t\t\t{ch}\t{characters}\t\t{max_length}\t\t{substring}")

                # Decrease current_end_index untill s[current_end_index] is different from s[current_start_index]
                current_end_index = current_end_index - 1
                while current_end_index >= current_start_index + 1 and s[current_end_index] != s[current_start_index]:
                    current_end_index -= 1

                characters = set()
                if current_end_index >= current_start_index:
                    for c in s[current_start_index: current_end_index]:
                        characters.add(c)
                print(
                    f"{num_iter}\t\t{current_start_index}\t\t\t{current_end_index}\t\t\t{ch}\t{characters}\t\t{max_length}\t\t{substring}")
                num_iter += 1
            print(f"*********finished {current_start_index} {current_end_index} ***************")
            return max_length

        def length_of_longest_substring_working(self, s: str) -> int:
            if len(s) <= 1:
                return len(s)
            current_longest = 1
            characters = set()
            substring = ""
            current_end_index = len(s)
            current_start_index = current_end_index - 1
            ch = s[current_start_index]
            substring = s[current_start_index:current_start_index]
            max_length = 0

            while current_end_index > 0 and current_start_index > 0:
                # print(current_start_index, current_end_index, ch, characters,  max_length, substring,ch)
                while current_start_index >= 0 and ch not in characters:
                    characters.add(ch)
                    current_start_index -= 1
                    ch = s[current_start_index]
                if current_start_index == -1:
                    max_substring = (current_start_index + 1, current_end_index)
                    substring = s[current_start_index + 1:current_end_index]
                    if len(substring) > max_length:
                        max_length = len(substring)
                    break
                max_substring = (current_start_index + 1, current_end_index)

                substring = s[current_start_index + 1:current_end_index]
                if len(substring) > max_length:
                    max_length = len(substring)

                current_end_index = current_end_index - 1
                while current_end_index >= current_start_index and s[current_end_index] != s[current_start_index]:
                    current_end_index -= 1
                characters = set()
                if current_end_index >= current_start_index + 1:
                    for c in s[current_start_index + 1: current_end_index]:
                        characters.add(c)
            return max_length

print(Solution().length_of_longest_substring_not_working("abcabcbb"))