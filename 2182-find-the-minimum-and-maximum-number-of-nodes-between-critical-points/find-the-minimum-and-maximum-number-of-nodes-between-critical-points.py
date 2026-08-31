class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            next_node = curr.next

            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    first = pos
                else:
                    minDist = min(minDist, pos - last)

                last = pos

            prev = curr
            curr = next_node
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [minDist, last - first]