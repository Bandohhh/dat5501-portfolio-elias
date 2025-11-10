import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# --- 1. Load and Clean Data ---
# The CSV filename is assumed to be in your working directory
filename = 'HistoricalData_1762772785970.csv'

df = pd.read_csv(filename)

# Parse date column into pandas datetime object and sort by date
# Makes chronological calculations correct
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df = df.sort_values(by='Date')

# Remove currency symbols and convert to numeric float
# Works for both dollar and pound signs
# (add more to regex if needed for other currencies)
df['Close/Last'] = df['Close/Last'].replace(r'[\$,£]', '', regex=True).astype(float)

# Calculate daily price change (diff() shifts so first value is NaN)
df['Daily Price Change'] = df['Close/Last'].diff()

# Get numpy array of daily changes, dropping the first NaN
changes = df['Daily Price Change'].dropna().values

# --- 2. Measure Sort Times over All Data Points ---
n_min = 7
n_max = min(365, len(changes))  # Use up to 365 days, or your data's max
n_values = np.arange(n_min, n_max + 1)
sort_times = []

for n in n_values:
    arr = changes[:n]  # Use ALL data points for slice 0:n
    start = time.perf_counter()
    np.sort(arr)
    end = time.perf_counter()
    sort_times.append(end - start)

# --- 3. Scale Theoretical n log n for Visual Comparison ---
# Find scaling factor to match the first measured sort time, so the curves overlay
C = sort_times[0] / (n_values[0] * np.log(n_values[0]))
nlogn_curve = C * n_values * np.log(n_values)

# --- 4. Plot Results ---
plt.figure(figsize=(10, 6))
plt.plot(n_values, sort_times, label='Measured sort time T', marker='.')
plt.plot(n_values, nlogn_curve, linestyle='--', label=r'Scaled $n \log n$ (theory)')
plt.xlabel('n (Number of days)')
plt.ylabel('T (Sorting time, seconds)')
plt.title('Sorting Time T vs n for Daily Price Changes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
