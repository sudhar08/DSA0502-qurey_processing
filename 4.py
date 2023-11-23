import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:/Users/12202/Downloads/archive (1)/GOOGL.csv')
# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Define the start and end dates
start_date = '2020-04-06'
end_date = '2020-04-23'

# Filter the data to include only the rows within the specified date range
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Create a line plot of the historical stock prices
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['date'], filtered_data['close'], marker='o', linestyle='-', color='b', label='Alphabet Inc. Stock Price')
plt.title('Historical Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()
