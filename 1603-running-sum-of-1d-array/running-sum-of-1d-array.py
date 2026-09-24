class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total

        return nums