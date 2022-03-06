class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits_present = [int(ch) for ch in time if ch != ":"]
        print(digits_present)
        index = 4

        current_digit = int(time[index])
        digits_for_replacement = [digit for digit in digits_present if digit < current_digit]
        if len(digits_present) == 0:
            index = index - 1



Solution().nextClosestTime("23:48")