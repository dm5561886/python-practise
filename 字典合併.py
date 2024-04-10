# 方法一
from collections import ChainMap
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d = {}
d.update(dic1)
d.update(dic2)
d.update(dic3)
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法二
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# 使用展開字典的方式，將這三個字典合併成一個新字典 d，並指定給它。
d = {**dic1, **dic2, **dic3}
# 輸出合併後的字典
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法三
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# 將這三個字典進行合併，先透過 list(dic.items()) 將字典轉成由 (key, value) 組成的列表
d = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
# 輸出合併後的字典
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 方法四
# collections 模組中的 ChainMap 類別，它可以將多個字典串連成一個映射對象
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d = dict(ChainMap(dic1, dic2, dic3))
print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
