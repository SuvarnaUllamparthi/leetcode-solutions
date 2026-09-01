from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litter = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        if k == 0:
            return 0

        index = {pos: i for i, pos in enumerate(litter)}
        all_mask = (1 << k) - 1

        # state: (row, col, energy_left, collected_mask)
        q = deque([(start[0], start[1], energy, 0)])
        visited = {(start[0], start[1], energy, 0)}

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == all_mask:
                    return steps

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1

                    if ne < 0:
                        continue

                    nmask = mask

                    if classroom[nr][nc] == 'L':
                        nmask |= 1 << index[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            steps += 1

        return -1