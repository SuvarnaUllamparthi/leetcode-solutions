class Solution:
    def uniformArray(self, nums1):
        has_odd = any(x % 2 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        if not has_odd or not has_even:
            return True

        # If both parities exist, every element can be made odd
        # by subtracting an element of opposite parity.
        # For n >= 2, each index has another element available.
        return True