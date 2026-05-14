class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for i in tokens:
            if i == '+' and stack:
                val = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == '-' and stack:
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == '*' and stack:
                val = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == '/' and stack:
                val = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(i))
                val = stack[-1]
        return val