class Solution:
    def minInsertions(self, s):
        open_count = 0
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # Check for a pair of closing brackets
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1

            i += 1

        # Each unmatched '(' needs two ')'
        insertions += open_count * 2

        return insertions