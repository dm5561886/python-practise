def containsDuplicate(nuns):
    dic = {}
    for i in nuns:
        if i not in dic:
            dic[i] = 1
        else:
            return True
    return False


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
