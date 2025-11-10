import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Set Seaborn style
sns.set(style='whitegrid', context='talk')

# Load and clean data
df = pd.read_csv('HistoricalData_1762772785970.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df.sort_values('Date', inplace=True)

# Convert price column to float
df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)

# Calculate daily price change
df['Daily Price Change'] = df['Close/Last'].diff()

# Prepare data for sorting time analysis
price_changes = df['Daily Price Change'].dropna().to_numpy()
timings = [
    time.perf_counter() - time.perf_counter()  # placeholder for initial value
    for _ in range(7)
]

for i in range(7, len(price_changes)):
    start = time.perf_counter()
    sorted(price_changes[:i])
    end = time.perf_counter()
    timings.append(end - start)

# X-axis values
x = np.arange(7, len(timings))

# Plotting
plt.figure(figsize=(10, 5))
sns.scatterplot(x=x, y=timings[7:], color='royalblue', edgecolor='white', s=80)

plt.title('Daily Price Changes', fontsize=16)
plt.xlabel('Number of Price Changes Sorted', fontsize=14)
plt.ylabel('Time (seconds)', fontsize=14)
plt.tight_layout()
plt.show()
