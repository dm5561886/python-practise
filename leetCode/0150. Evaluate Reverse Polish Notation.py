def evalRPN(tokens):
    # 使用堆疊概念解
    math = ["*", "/", "+", "-"]
    stack = []
    for i in tokens:
        if i not in math:
            stack.append(int(i))
        else:
            last = stack.pop()
            first = stack.pop()
            if i == "*":
                stack.append(first * last)
            elif i == "/":
                stack.append(int(first / last))
            elif i == "+":
                stack.append(first + last)
            else:
                stack.append(first - last)
    return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
