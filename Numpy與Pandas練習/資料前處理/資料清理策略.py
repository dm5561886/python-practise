import numpy as np
import pandas as pd
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
            'age': [42, np.nan, 36, 24, 73],
            'sex': ['m', np.nan, 'f', 'm', 'f'],
            'preTestScore': [4, np.nan, np.nan, 2, 3],
            'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns=[
                  'first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

# Drop missing observations刪除所有含有缺失值的觀測值（列）
df1 = df.dropna()
# Drop rows where all cells in that row is NA
# how='all'參數指定只有在一列的所有單元格都是遺漏值時，才刪除
df.dropna(how='all')
# Create a new column full of missing values
df['new_column'] = np.nan
# Fill in missing data with zeros
df3 = df.fillna(0)
# Fill in missing in preTestScore with the mean value of preTestScore
df['preTestScore'].fillna(df['preTestScore'].mean(), inplace=True)
# Fill in missing in postTestScore with each sex’s mean value of postTestScore
# 以每個性別的 postTestScore 平均值填入 postTestScore 中的缺失值
# transform('mean')會計算每個群組的平均值，然後將這些平均值根據原始數據的索引位置，填充到相應的位置上
df['postTestScore'].fillna(df.groupby(
    'sex')['postTestScore'].transform('mean'), inplace=True)

# Select some rows but ignore the missing data points
df4 = df.dropna(axis=0)
