import pandas as pd
data = {
    'Text_Column': ['apple', 'Banana', 'CHERRY', 'date', 'Elderberry', 'Fig', 'Grape']
}
df = pd.DataFrame(data)
column_to_swap = 'Text_Column'
df[column_to_swap] = df[column_to_swap].apply(lambda x: x.swapcase())
print(df)
