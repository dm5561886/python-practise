def isAnagram(s, t):
    dic_s = {}
    dic_t = {}
    for i in s:
        if i not in dic_s:
            dic_s[i] = 1
        else:
            dic_s[i] += 1

    for j in t:
        if j not in dic_t:
            dic_t[j] = 1
        else:
            dic_t[j] += 1

    for x in s:
        # 檢查 s的字是否在dict和出現次數是否相同
        if x not in dic_t or dic_s[x] != dic_t[x]:
            return False

    return True


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
