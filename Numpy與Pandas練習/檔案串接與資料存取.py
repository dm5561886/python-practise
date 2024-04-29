import pandas as pd

data = pd.read_csv(
    'https://raw.githubusercontent.com/kiang/pharmacies/master/data.csv')

x = data.groupby('縣市')
result = x.agg({'醫事機構名稱': 'count'}).sort_values(
    by='醫事機構名稱', ascending=False).head(5)
print(result)
