# 方法一(無函式)
nums = [2, 7, 11, 15]
target = 18
n = len(nums)
d = []
for i in range(n):
    for j in range(i+1, n):
        if nums[i]+nums[j] == target:
            d.append(i)
            d.append(j)

print(d)  # [0,1]
