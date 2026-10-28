class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in index_map:
                if i - index_map[num] <= k:
                    return True
            index_map[num] = i
        return False