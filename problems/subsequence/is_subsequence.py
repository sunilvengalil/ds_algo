class Solution:
    """
    1. Keep two pointers left and right (right > left) to point to a specific position in the larger string t. Initialize left =0, right = 1
    2. Initialize index_to_subsequence = 0 - this points to a position in s
    3. Seek left pointer - Move left to point to the first occurance of character at s[index_to_subsequence]
    4. If left pointer crosses the last index of t , return False
    5. if index_to_subsequence is the last index return True
    6. set right = left
    7. While index_to_subsequence is less than the len(s)
        a) increment index_to_subsequence
        b) Seek right pointer - move right pointer until t[right] = s[index_to_subsequence
        ]
        c) if right has crossed the end of t, return False
    8. Return True

    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True
        index_to_subsequence = 0
        left = 0
        # Seek the left pointer
        while left <= len(t) - len(s) and t[left] != s[index_to_subsequence]:
            left += 1
        if left > len(t) - len(s):
            return False
        right = left
        while index_to_subsequence < len(s) - 1:
            index_to_subsequence += 1
            # Seek the right pointer
            right += 1
            while right < len(t) and t[right] != s[index_to_subsequence]:
                right += 1
            if right == len(t):
                return False
        return True


if __name__ == "__main__":

    e = [True, True, False, True]
    r = []
    s = Solution()
    test_cases = [("a", "dabc"), ("ac", "dabc"),("x", "dabc"), ("", "dabc")]
    test_cases = [test_cases[1]]
    for t in test_cases:
        r.append(s.isSubsequence(t[0], t[1]))
    for t, expected, result in zip(test_cases, e, r):
        if expected != result:
            print(f"Testcase failed: {t}")
            raise Exception("Testcase failed")
    print("All tests passed")


