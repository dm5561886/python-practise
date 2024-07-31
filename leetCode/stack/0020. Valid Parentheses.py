def isValid(s):
    # 使用堆疊(Stack)
    stack = []
    # 遍歷字串
    for char in s:
        # 如果是左括號，就加入堆疊中等待配對
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            # 若堆疊為空，回傳 False
            if len(stack) == 0:
                return False
            # 如果堆疊裡有等待配對的左括號即配對成功，刪除堆疊裡的左括號
            # pop()預設刪最後一個
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                # 若堆疊裡為右括號，回傳False
                return False
    # 字串走訪完，且堆疊為空，回傳True
    return len(stack) == 0


s = "(({]))"
print(isValid(s))
