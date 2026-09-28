class Solution(object):
    def sumFourDivisors(self, nums):
        total = 0
        for n in nums:
            count = 0
            divisor_sum = 0
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    count += 1
                    divisor_sum += i
                    if i != n // i:
                        count += 1
                        divisor_sum += n // i
            if count == 4:
                total += divisor_sum
        return total