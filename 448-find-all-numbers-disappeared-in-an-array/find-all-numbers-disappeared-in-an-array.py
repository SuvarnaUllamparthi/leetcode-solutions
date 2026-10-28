class Solution:
    def findDisappearedNumbers(self, nums):

        num_set = set(nums)

        answer = []

        n = len(nums)

        for i in range(1, n + 1):

            if i not in num_set:

                answer.append(i)

        return answer