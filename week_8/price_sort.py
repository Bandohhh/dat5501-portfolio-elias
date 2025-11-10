import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Palantir price data from a CSV file
palantir_price_data_df = pd.read_csv('HistoricalData_1762772785970.csv')

#show all rows
pd.set_option('display.max_rows', None)

print(palantir_price_data_df)

# calculate daily price change

palantir_price_data_df['Close/Last'] = palantir_price_data_df['Close/Last'].replace('[\$,]', '', regex=True).astype(float) # Remove dollar signs and convert to float

palantir_price_data_df['Daily Price Change'] = palantir_price_data_df['Close/Last'].diff()

# Display the updated DataFrame with daily price changes
print(palantir_price_data_df)



