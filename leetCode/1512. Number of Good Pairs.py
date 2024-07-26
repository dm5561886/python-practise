def numIdenticalPairs(nums):
    count = 0  # 配對計數
    dic = {}  # 雜湊表，計算重複出現的數字
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            count += dic[i]
            dic[i] += 1

    return count


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
