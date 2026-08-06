class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            x = n

            if x == 0:
                product = 0
            else:
                while x > 0:
                    product *= x % 10
                    x //= 10

            if product % t == 0:
                return n

            n += 1