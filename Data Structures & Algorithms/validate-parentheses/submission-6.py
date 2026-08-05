class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
            }   

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                top = stack[-1]
                if pairs[char] == top:
                    stack.pop()
                else:
                    return False
        return not stack
            
            
        