"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/467/
"""

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        result = True
        for ch in s:
            if ch in ["(","[","{"]:
                stack.append(ch)
            elif ch == ")":
                if len(stack) == 0:
                    result = False
                    break
                matching = stack.pop()
                if matching != "(":
                    result = False
                    break
            elif ch == "]":
                if len(stack) == 0:
                    result = False
                    break
                matching = stack.pop()
                if matching != "[":
                    result = False
                    break
            elif ch == "}":
                if len(stack) == 0:
                    result = False
                    break
                matching = stack.pop()
                if matching != "{":
                    return False
                    break
        if  len(stack) > 0 :
            result = False

        return result

str = "()"
print(Solution().isValid(str))
str = "("
print(Solution().isValid(str))
str = ")"
print(Solution().isValid(str))
str = "(){}"
print(Solution().isValid(str))
str = "[(){}{}]"
print(Solution().isValid(str))
str = "([{([{}])}])"
print(Solution().isValid(str))
str = "({}[{}{}])"
print(Solution().isValid(str))
str = "()[{}[]()]"
print(Solution().isValid(str))