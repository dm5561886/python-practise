import pandas as pd
import numpy as np
#
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)
# - 1. filtered by first column > 20?
a = df[0] > 20
# - 2. filtered by first column + second column > 50
b = df[0] + df[1] > 50
# - 3. filtered by first column < 30 or second column > 30
c = (df[0] < 30) | (df[1] > 30)
# - 4. filtered by total sum of row > 100
# row > 100要讓每個欄相加
d = df.sum(axis=1) > 100  # axis=1 表示橫列(列)的加總
print(df[d])
