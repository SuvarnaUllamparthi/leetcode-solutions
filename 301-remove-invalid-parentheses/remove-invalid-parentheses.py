class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        level = {s}

        while True:
            result = []

            for string in level:
                if isValid(string):
                    result.append(string)

            if result:
                return result

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            level = next_level