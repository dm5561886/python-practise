import pandas as pd
import numpy as np

d = [
    {'city': 'Austin', 'visitor': 139, 'weekday': 'Sun'},
    {'city': 'Dallas', 'visitor': 237, 'weekday': 'Sun'},
    {'city': 'Austin', 'visitor': 326, 'weekday': 'Mon'},
    {'city': 'Dallas', 'visitor': 456, 'weekday': 'Mon'}
]

data = pd.DataFrame(d)
print(data)
x = data.groupby('weekday')  # 按照 "weekday" 的值進行分組
result = x.agg({'visitor': 'sum'}).sort_values(by='visitor')
print(result)
output = result.to_dict()['visitor']  # 將dataframe轉為dictionary
print(output)
