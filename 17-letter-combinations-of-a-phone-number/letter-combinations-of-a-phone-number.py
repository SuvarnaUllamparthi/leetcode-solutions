

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, path: str):
            # Base case: if path length equals digits length, add to result
            if index == len(digits):
                result.append(path)
                return
            
            # Get possible letters for current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result


