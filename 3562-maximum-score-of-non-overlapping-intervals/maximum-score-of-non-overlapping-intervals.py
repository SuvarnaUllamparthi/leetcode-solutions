class Solution:
    def maximumWeight(self, intervals):
        intervals = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(intervals)

        starts = [x[0] for x in intervals]

        import bisect

        nxt = []
        for l, r, w, idx in intervals:
            nxt.append(bisect.bisect_right(starts, r))

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = intervals[i]

            for cnt in range(5):
                best = dp[i + 1][cnt]

                if cnt < 4:
                    ni = nxt[i]
                    take_score = w + dp[ni][cnt + 1][0]
                    take_indices = tuple(sorted((idx,) + dp[ni][cnt + 1][1]))
                    take = (take_score, take_indices)

                    if take[0] > best[0] or (take[0] == best[0] and take[1] < best[1]):
                        best = take

                dp[i][cnt] = best

        return list(dp[0][0][1])