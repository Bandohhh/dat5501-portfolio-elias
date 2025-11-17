import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set seaborn style for all plots
sns.set_theme(style="whitegrid", palette="deep", context="notebook")

# Load the CSV
gold_price = pd.read_csv('week_8/thurs/price-per-kg-of-gold.csv')

# Drop columns we don't need
gold_price = gold_price.drop(columns=['Entity', 'Code'])

# Change the column name for clarity
gold_price = gold_price.rename(
    columns={'Gold (New York Market Price) (Laurence & Williamson (2017))': 'Price'}
)

# Filter the data as requested
gold_price = gold_price[(gold_price['Year'] <= 2015) & (gold_price['Year'] >= 1915)]

# Set up color palette for fits
fit_palette = sns.color_palette("husl", 9)

plt.figure(figsize=(12, 7))
sns.scatterplot(
    x='Year', y='Price', data=gold_price,
    color='navy', s=40, label='Original Data', edgecolor='w', linewidth=0.5
)

def n_polynomial_fit(order, color):
    # Fit and plot polynomial
    coeffs = np.polyfit(gold_price['Year'], gold_price['Price'], order)
    poly = np.poly1d(coeffs)
    x_vals = np.linspace(gold_price['Year'].min(), gold_price['Year'].max(), 300)
    y_vals = poly(x_vals)
    plt.plot(
        x_vals, y_vals, 
        color=color, 
        label=f'Fit Order {order}', 
        linewidth=2, 
        alpha=0.8
    )
    return poly

# Loop through polynomial orders with color palette
polynomials = []
for order, color in zip(range(1, 10), fit_palette):
    poly = n_polynomial_fit(order, color)
    polynomials.append(poly)

plt.xlabel('Year', fontsize=14)
plt.ylabel('Price per kg of Gold (USD)', fontsize=14)
plt.title('Gold Price (1915–2015)\nPolynomial Fits of Various Orders', fontsize=16)
plt.legend(title="Polynomial Fits", fontsize=12, title_fontsize=13, loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()

# Print the last polynomial fit coefficients
print(polynomials[-1])









