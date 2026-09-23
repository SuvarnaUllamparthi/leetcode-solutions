class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        total = 0
        while n > 0:
            digit = n % 10
            product = product * digit
            total = total + digit
            n = n // 10
        return product - total

        