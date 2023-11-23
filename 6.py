import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:/Users/12202/Downloads/archive (1)/GOOGL.csv")
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Define the start and end dates
start_date = '2020-04-06'
end_date = '2020-04-23'

# Filter the data to include only the rows within the specified date range
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Create a scatter plot of trading volume vs. stock prices
plt.figure(figsize=(12, 6))
plt.scatter(filtered_data['volume'], filtered_data['close'], color='b', label='Volume vs. Stock Prices')
plt.title('Trading Volume vs. Stock Prices of Alphabet Inc. Stock')
plt.xlabel('Volume')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()
