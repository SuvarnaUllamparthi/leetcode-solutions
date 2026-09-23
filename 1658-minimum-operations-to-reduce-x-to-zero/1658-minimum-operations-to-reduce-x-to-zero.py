class Solution:
    def minOperations(self, nums, x):

        total = sum(nums)
        target = total - x

        if target == 0:
            return len(nums)

        left = 0
        current = 0
        max_length = -1

        for right in range(len(nums)):
            current += nums[right]

            while current > target and left <= right:
                current -= nums[left]
                left += 1

            if current == target:
                max_length = max(max_length, right - left + 1)

        if max_length == -1:
            return -1

        return len(nums) - max_length