class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # If the current element occurs more than k times,
            # move left until the window becomes valid.
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans