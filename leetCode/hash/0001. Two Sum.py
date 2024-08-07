# 方法三
def twosum(nums, target):
    x = {}
    for i, num in enumerate(nums):  # 使用enumerate()函數轉換為索引序列
        diff = target-num  # 計算與目標值的差值，尋找的另一個數字
        if diff in x:
            return [x[diff], i]
        x[num] = i  # 將當前數字和 index 存入 x 中

    return []


nums = [2, 7, 11, 15]
target = 9
d = twosum(nums, target)
print(d)
