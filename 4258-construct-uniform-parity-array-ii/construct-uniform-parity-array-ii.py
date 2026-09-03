class Solution(object):
    def uniformArray(self, nums):
        a = min(nums)
        if a%2 == 1:      # min is odd, can make everything odd
            return True
        for i in nums:
            if i%2 == 1:  # min is even but odd exists, impossible
                return False
        return True       # all even already