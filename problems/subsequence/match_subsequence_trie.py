# https://leetcode.com/problems/number-of-matching-subsequences/

from typing import List

# Correct soln but time limit exceeded
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words_to_process = [w for w in words if len(w) <= len(s)]
        print(words_to_process)
        words_to_process_non_empty = [w for w in words_to_process if len(w) != 0]
        num_empty_soln = len(words_to_process) - len(words_to_process_non_empty)
        left_pointers = [-1] * len(words_to_process_non_empty)
        right_pointers = [-1] * len(words_to_process_non_empty)
        index_to_subsequence = [-1] * len(words_to_process_non_empty)
        num_matching_words = 0
        print(words_to_process_non_empty)
        words_bucketted = [None] * 26
        for w in words_to_process_non_empty:
            ch = ord(w[0]) - ord('a')
            if words_bucketted[ch] is None:
                words_bucketted[ch] = [w]
            else:
                words_bucketted.append(w)

        for ch_index, ch in enumerate(s):
            words_to_remove = []


            for word_no, w in enumerate(words_bucketted[ord(ch) - ord('a')]):
                

                if left_pointers[word_no] == -1:
                    # left was not found for this subsequence yet
                    if w[0] == ch:
                        # left found for this subseauence now
                        left_pointers[word_no] = ch_index
                        index_to_subsequence[word_no] = 0
                        right_pointers[word_no] = ch_index
                        if len(w) == 1:
                            num_matching_words += 1
                            words_to_remove.append(word_no)
                        else:
                            index_to_subsequence[word_no] += 1

                else:
                    # left was already found for this subsequence. update the index_to_subsequence and right based on current character
                    if w[index_to_subsequence[word_no]] ==ch:
                        right_pointers[word_no] = ch_index
                        if index_to_subsequence[word_no] == len(w) - 1:
                            # last character of subsequence w is found
                            num_matching_words += 1
                            words_to_remove.append(word_no)
                        else:
                            index_to_subsequence[word_no] += 1

            for word_no in reversed(words_to_remove):
                words_to_process_non_empty.pop(word_no)
                left_pointers.pop(word_no)
                right_pointers.pop(word_no)
                index_to_subsequence.pop(word_no)


            print(words_to_process_non_empty)
            print(ch, ch_index, left_pointers)
            print(ch, ch_index, right_pointers)
            print(ch, ch_index, index_to_subsequence)
            print("**************************")
        return num_matching_words + num_empty_soln

if __name__ == "__main__":
    s = Solution()
    r = s.numMatchingSubseq("xaybcdz", ["abc", "xyz", "a", "ad"])
    print(r)