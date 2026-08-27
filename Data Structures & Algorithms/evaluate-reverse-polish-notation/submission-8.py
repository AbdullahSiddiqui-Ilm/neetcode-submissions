class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for cur in tokens:
            if cur not in '+-*/':
                stack.append(int(cur))
            elif cur == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif cur == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif cur == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif cur == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
        return stack[-1]