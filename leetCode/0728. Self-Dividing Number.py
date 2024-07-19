def is_self_dividing(n):  # 判斷是否為字除數
    digits = []
    for num in str(n):
        digits.append(int(num))
    for d in digits:
        if d == 0 or n % d != 0:
            return False
    return True


def number(left, right):  # 找出差距最大的 Self-Dividing Number
    numbers = []
    for i in range(left, right+1):  # 把是字除數的放到list裡
        if is_self_dividing(i):
            numbers.append(i)

    max_diff = 0  # 用來儲存兩個字除數相減的結果
    max_diff_pair = None
    for i in range(len(numbers)-1):
        if numbers[i+1]-numbers[i] > max_diff:  # 如果鄉檢結果大於上一組的結果
            max_diff_pair = (numbers[i], numbers[i+1])  # 存放差距最大兩數
            max_diff = numbers[i+1]-numbers[i]
    return max_diff_pair


a, b = int(input("請輸入第一個數字:")), int(input("請輸入最後一個數字:"))  # 11, 20
max_diff_pair = number(a, b)
print(max_diff_pair)  # (12, 15)
