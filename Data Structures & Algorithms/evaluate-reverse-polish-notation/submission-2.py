class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNum = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                num1 = stackNum.pop()
                num2 = stackNum.pop()
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num2 - num1
                elif t == '*':
                    res = num1 * num2
                elif t == '/':
                    res = num2 / num1
                stackNum.append(int(res))
            else:
                stackNum.append(int(t))
        return stackNum.pop()
