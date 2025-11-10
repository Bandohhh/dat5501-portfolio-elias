import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Load the CSV using your specified filename
palantir_price_data_df = pd.read_csv('HistoricalData_1762772785970.csv')

# Sort dates in ascending order and parse dates
palantir_price_data_df['Date'] = pd.to_datetime(palantir_price_data_df['Date'], format='%m/%d/%Y')
palantir_price_data_df = palantir_price_data_df.sort_values(by='Date', ascending=True)

# Optionally show all rows when printing (can be commented out)
pd.set_option('display.max_rows', None)

# Clean 'Close/Last' column, remove dollar signs, and convert to float
palantir_price_data_df['Close/Last'] = palantir_price_data_df['Close/Last'].replace(r'[\$,£]', '', regex=True).astype(float)

# Calculate daily price change as a new column
palantir_price_data_df['Daily Price Change'] = palantir_price_data_df['Close/Last'].diff()

# Convert daily price changes to a NumPy array, dropping the first NaN
price_changes = palantir_price_data_df['Daily Price Change'].dropna().to_numpy()

# Prepare to measure sort times for increasing n
n_min = 7
n_max = min(365, len(price_changes))  # Use up to 365 points, or all if less
n_values = np.arange(n_min, n_max + 1)
sort_times = []

for n in n_values:
    array_to_sort = price_changes[:n]
    start_time = time.perf_counter()
    sorted_array = np.sort(array_to_sort)
    end_time = time.perf_counter()
    sort_times.append(end_time - start_time)

# Scale the theoretical n log n curve for fair visual comparison
scaling_constant = sort_times[0] / (n_values[0] * np.log(n_values[0]))
nlogn_curve = scaling_constant * n_values * np.log(n_values)

# Plotting the measured and theoretical sorting times
plt.figure(figsize=(10, 5))
plt.plot(n_values, sort_times, label='Measured sort time (T)', marker='o', linestyle='-', color='blue')
plt.plot(n_values, nlogn_curve, linestyle='--', label=r'Scaled $n \log n$ (Theory)', color='red')
plt.title('Sorting Time T vs n for Palantir Daily Price Changes')
plt.xlabel('Number of Daily Price Changes Sorted (n)')
plt.ylabel('Sorting Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
