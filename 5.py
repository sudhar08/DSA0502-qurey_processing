import pandas as pd
import matplotlib.pyplot as plt

# Read the historical stock price data from a CSV file
df = pd.read_csv(r"C:/Users/12202/Downloads/archive (1)/GOOGL.csv")
# Create a DataFrame from the provided data (you can replace this with your data)

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Define the start and end dates
start_date = '2020-04-06'
end_date = '2020-04-23'

# Filter the data to include only the rows within the specified date range
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# Create a bar plot of the trading volume
plt.figure(figsize=(12, 6))
plt.bar(filtered_data['date'], filtered_data['volume'], color='b', label='Trading Volume')
plt.title('Trading Volume of Alphabet Inc. Stock')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(axis='y')
plt.show()
