def findDuplicates(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    arry = []
    for k, v in dic.items():
        if v > 1:
            arry.append(k)
            arry.sort()

    return arry


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))
