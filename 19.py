import pandas as pd
data = {
    'Year': ['1986', '1986', '1985', '1986', '1987'],
    'Africa': ['Africa', 'Americas', 'Americas', 'Americas', 'Africa'],
    'Americas': ['Americas', 'WHO region', 'Western Pacific', 'Americas', 'Việt Nam'],
    'Country': ['Việt Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [1.62, 4.27, 0.00, 0.50, 1.98]
}
df = pd.DataFrame(data)
print("Dimensions (Shape) of the DataFrame:", df.shape)
column_names = df.columns
print("Column Names:")
for column in column_names:
    print(column)
