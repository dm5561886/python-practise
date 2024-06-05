import pandas as pd
import numpy as np

data = pd.DataFrame({
    'col1': [5, 12, 8, np.nan],
    'col2': [16, 9, np.nan, 4],
    'col3': [11, 3, 7, 20]
})

# 檢查缺失值
a = data.isnull()
print(a)
