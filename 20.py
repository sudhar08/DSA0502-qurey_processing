import pandas as pd
data = {
    'Text_Column': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
}
df = pd.DataFrame(data)
substring = 'err'
indexes = df[df['Text_Column'].str.contains(substring, case=False)].index
print("Indexes of rows containing the substring:", indexes)
