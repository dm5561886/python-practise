# 將字串當中的出現的 not … at all 換成 good ， 中間的「…」代表的是任意字串或沒有內容
s = input("輸入字串:")  # This company is not poor at all.
# 找到字串 s 中的 'not' 子字串在 s 中的位置
c1 = s.find('not')
# 找到字串 s 中的 'at all' 子字串在 s 中的位置，再加上 6 個字元的位置，得到子字串結束的位置
c2 = s.find('at all') + 6
# 利用字串的切片（slicing）功能，取出 'not' 子字串前的字串、'at all' 子字串後的字串，並插入 'good'，組成新的字串
d = s[0:c1] + 'good' + s[c2:len(s)]
print(d)  # This company is good.

# 方法二
s = input()
# 將字串 s 以 "not" 分割，取得分割後的第一個子字串，也就是 "not" 之前的部分
s1 = s.split('not')[0]
# 將字串 s 以 "at all" 分割，取得分割後的第二個子字串，也就是 "at all" 之後的部分
s2 = s.split('at all')[1]
# 將 s1、"good" 和 s2 結合成新的字串 d
d = f'{s1}good{s2}'
print(d)
