class Solution:
    def toHex(self, num):

        if num == 0:
            return "0"

        if num < 0:
            num = num + (1 << 32)

        digits = "0123456789abcdef"
        result = ""

        while num > 0:
            remainder = num % 16
            result = digits[remainder] + result
            num = num // 16

        return result