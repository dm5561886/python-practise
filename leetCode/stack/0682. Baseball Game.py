def calPoints(ops):
    r = ['+', 'D', 'C']
    stack = []
    for i in ops:
        if i not in r:
            stack.append(int(i))
        else:
            if i == '+' and len(stack) >= 2:
                stack.append(stack[-1]+stack[-2])
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == 'C':
                stack.pop()
    return sum(stack)


ops = ["5",  "C"]
print(calPoints(ops))
