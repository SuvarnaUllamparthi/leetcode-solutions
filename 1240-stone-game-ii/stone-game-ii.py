class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones the current player
        # can collect starting from index i with M
        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Current player takes X piles.
                # The opponent gets the best they can from the rest.
                opponent = dp(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)