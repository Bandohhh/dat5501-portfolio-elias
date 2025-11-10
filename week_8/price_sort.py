import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

# Load the CSV 
palantir_price_data_df = pd.read_csv('HistoricalData_1762772785970.csv')
# Sort the dates in ascending order
palantir_price_data_df['Date'] = pd.to_datetime(palantir_price_data_df['Date'], format='%m/%d/%Y')
palantir_price_data_df_price_data_df = palantir_price_data_df.sort_values(by='Date', ascending=True)

# Setting to show all rows when printing the dataframe
pd.set_option('display.max_rows', None)

#print (asset_price_data_df)

# Calculate daily price change
palantir_price_data_df['Close/Last'] = palantir_price_data_df['Close/Last'].replace('[\$,]', '', regex=True).astype(float) # Remove dollar signs and convert to float

palantir_price_data_df['Daily Price Change'] = palantir_price_data_df['Close/Last'].diff()
#print (asset_price_data_df)


# Move the price changes column to an array for plotting
price_changes = palantir_price_data_df['Daily Price Change'].dropna().to_numpy()
times = []

for i in range(7, len(price_changes)):
    
    array_to_sort = price_changes[:i]
    
    start_time = time.perf_counter()
    # Sort the array
    sorted_array = sorted(array_to_sort)
    end_time = time.perf_counter()
    
    time_taken = end_time - start_time
    times.append(time_taken)

# Create x-axis values
x_values = np.arange(7, len(times)+7)

# Calculate n log n values for comparison
n_log_n = x_values * np.log(x_values) 

# Plot the graph
plt.figure(figsize=(8, 4))

# Plot scatter 
plt.scatter(x_values, times, marker='o', linestyle='-', color='blue')
plt.title('Daily Price Changes')
plt.xlabel('Number of Price Changes Sorted')
plt.ylabel('Time')
plt.grid(True)
plt.tight_layout()
plt.show()