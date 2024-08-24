from collections import deque


def firstUniqChar(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for index, str in enumerate(s):
        if dic[str] == 1:
            return index
    return -1


s = "loveleetcode"
print(firstUniqChar(s))
