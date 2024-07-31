def maximizeSum(nums, k):
    score = 0
    for i in range(k):
        max_n = max(nums)
        score += max_n
        max_n += 1
        nums.append(max_n)
    return score


nums = [1, 2, 3, 4, 5]
k = 3
print(maximizeSum(nums, k))
