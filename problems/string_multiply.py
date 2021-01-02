class Solution:
    def _add(self, num1: str, num2: str) -> str:
        min_length = min(len(num1), len(num2))
        result = ["0"] * (max(len(num1), len(num2)) + 1)
        carry = 0
        # print(num1,num2)
        for pos in range(min_length):
            digit_sum = int(num1[len(num1) - pos - 1]) + int(num2[len(num2) - pos - 1]) + carry
            if digit_sum >= 10:
                carry = 1
                digit_sum = digit_sum - 10
            else:
                carry = 0
            # print(len(num2) - pos - 1)
            result[len(result) - pos - 1] = str(digit_sum)

        bigger = None
        if len(num1) > len(num2):
            bigger = num1
        elif len(num1) < len(num2):
            bigger = num2
        if bigger is not None:
            left_out = len(bigger) - min_length
            for pos in range(left_out):
                digit_sum = carry + int(bigger[left_out - pos - 1])
                if digit_sum >= 10:
                    carry = 1
                    digit_sum = digit_sum - 10
                else:
                    carry = 0
                result[left_out - pos] =  str(digit_sum)

        if carry == 1:
            result[0] = "1"
        else:
            result = result[1:]
        # print(result)
        return "".join(result)

    def _multiply(self, num: str, digit: int) -> str:
        """
        Multiply `num` by digit
        """
        if digit == 0:
            return ["0"]
        result = ["0"] * (len(num) + 1)
        carry = 0
        place_value = 1
        for pos in range(len(num) - 1, -1, -1):
            product = int(num[pos]) * digit + carry
            if product >= 10:
                carry = product // 10
                product = product % 10
            else:
                carry = 0
            result[pos + 1] = str(product)

        if carry > 0:
            result[0] = str(carry)
        else:
            result = result[1:]
        return result

    def multiply(self, num1: str, num2: str) -> str:
        result = ['0']
        num_zeros_for_place_value = 0
        for pos in range(len(num2) - 1, -1, -1):
            digit = num2[pos]
            num1_times_digit = self._multiply(num1, int(digit))
            #print(num1_times_digit)
            if not (len(num1_times_digit) == 1 and num1_times_digit[0] == "0"):
                for i in range(num_zeros_for_place_value):
                    num1_times_digit.append("0")
            num_zeros_for_place_value += 1
            result = list(self._add("".join(result), "".join(num1_times_digit)))
        return "".join(result)

