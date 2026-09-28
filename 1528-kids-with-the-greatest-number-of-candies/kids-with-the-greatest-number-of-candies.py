class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
        