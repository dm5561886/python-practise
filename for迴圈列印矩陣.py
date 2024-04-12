matrix = []
rows = int(input("請輸入矩陣列數:"))
cols = int(input("請輸入矩陣行數:"))
for i in range(rows):
    matrix.append([])
    for j in range(cols):
        a = int(input("請輸入矩陣的元素(由上往下逐獵輸入):"))
        matrix[i].append(a)

print(matrix)
