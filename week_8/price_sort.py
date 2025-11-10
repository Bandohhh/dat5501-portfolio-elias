import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Load the Palantir price data from a CSV file
df = pd.read_csv('HistoricalData_1762772785970.csv')

# Parse dates and ensure ascending order
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df = df.sort_values(by='Date', ascending=True)

# Clean and convert closing price column
df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)

# Calculate daily price changes
df['Daily Price Change'] = df['Close/Last'].diff()

# Remove the first NaN row from the diff operation
daily_changes = df['Daily Price Change'].dropna().values

# Set up arrays for timing sorting over increasing n
n_values = np.arange(7, min(len(daily_changes), 366), 10)  # n from 7 to up to 365 by 10
sort_times = []

for n in n_values:
    sample = daily_changes[:n]
    start = time.time()
    np.sort(sample)
    end = time.time()
    sort_times.append(end - start)

# Plotting T vs n and n log n scaling
plt.figure(figsize=(10, 6))
plt.plot(n_values, sort_times, label='Sort Time (seconds)', marker='o')

# Overlay n log n complexity for reference
scaled_nlogn = sort_times[0] * n_values * np.log(n_values) / (n_values[0] * np.log(n_values[0]))
plt.plot(n_values, scaled_nlogn, label=r"Scaled $n \log n$", linestyle='--')

plt.xlabel('n (Number of Days)')
plt.ylabel('T (Time to Sort in Seconds)')
plt.title('Sorting Time T vs n for Daily Price Changes')
plt.legend()
plt.grid(True)
plt.show()

# Optional: display processed DataFrame
print(df)




