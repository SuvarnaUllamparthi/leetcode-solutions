from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)

        # Check if any outside method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Remove suspicious methods
        return [i for i in range(n) if i not in suspicious]