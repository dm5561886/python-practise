def romanToInt(s):
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for i in range(len(s)):
        # 當遍歷到最後一個字時就加起來
        if i == len(s)-1 or dic[s[i]] >= dic[s[i+1]]:
            num += dic[s[i]]
        else:
            num -= dic[s[i]]
    return num


s = 'LVIII'
print(romanToInt(s))
