# 方法二
def twosum(nums, target):
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []


nums = [2, 7, 11, 15]
target = 9
n = len(nums)
d = twosum(nums, target)
print(d)
