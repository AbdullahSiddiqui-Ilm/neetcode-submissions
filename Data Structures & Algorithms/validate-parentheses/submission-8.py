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
                elif pairs[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
            
            
        