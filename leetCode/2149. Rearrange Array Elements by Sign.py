def rearrangeArray(nums):
    neg_num = []
    pos_num = []
    for i in nums:
        if i > 0:
            pos_num.append(i)
        else:
            neg_num.append(i)

    output = []
    for i in range(len(pos_num)):
        output.append(pos_num[i])
        output.append(neg_num[i])
    return print(output)


nums = [3, 1, -2, -5, 2, -4]
rearrangeArray(nums)
