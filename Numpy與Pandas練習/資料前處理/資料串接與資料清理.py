import pandas as pd
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# Check if df has any missing values檢查 DataFrame 是否有任何缺失值
check_null = df.isnull().values.any()
# Count the number of missing values in each column and find the maximum number of missing values.
# 計算每列中缺失值的數量，並找到缺失值數量最多的列
missing_values_count = df.isnull().sum()
missing_maxnum = missing_values_count.max()
# How to replace missing values of `multiple numeric` columns with the mean?
int_type = df.select_dtypes(include='number').columns  # 找出數值類型的欄位
for col in int_type:
    df[col].fillna(df[col].mean(), inplace=True)
# Calculate the average price of different manufacturers.
manufacturers_price = df.groupby('Manufacturer')['Price'].mean()
# How to replace missing values of `price` columns with the mean depending on its manufacturers?
df['Price'] = df['Price'].fillna(df.groupby('Manufacturer')[
                                 'Price'].transform('mean'))
print(df)
