import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dictionary to store chi squared values for different polynomial orders
chi_squared_values = {}

# Load the CSV
gold_price = pd.read_csv('week_8/thurs/price-per-kg-of-gold.csv')

# Drop columns we don't need
columns_to_drop = ['Entity', 'Code']
gold_price = gold_price.drop(columns=columns_to_drop)

pd.set_option('display.max_rows', None)  # Display all rows

# Change column name for convenience
gold_price = gold_price.rename(
    columns={'Gold (New York Market Price) (Laurence & Williamson (2017))': 'Price'}
)

# Create subsample: last 100 years, no last 10 years
gold_price = gold_price[(gold_price['Year'] <= 2015) & (gold_price['Year'] >= 1915)]

# --- UPDATED FUNCTION DEFINITION STARTS HERE ---
def n_polynomial_fit(order):
    # Check: You need at least (order + 1) data points to fit this polynomial safely!
    if len(gold_price) <= order:
        raise ValueError(
            f"Not enough data points ({len(gold_price)}) for a polynomial of order {order}. Reduce the order."
        )
    coefficients, covariance = np.polyfit(
        gold_price['Year'],
        gold_price['Price'],
        order,
        cov=True
    )
    polynomial = np.poly1d(coefficients)

    # Generate x values for plotting the fitted Curve
    x_values = np.linspace(gold_price['Year'].min(), gold_price['Year'].max(), 100)
    y_values = polynomial(x_values)

    # Residuals and chi squared value for the fit
    residuals = gold_price['Price'] - polynomial(gold_price['Year'])
    chi_squared = np.sum((residuals ** 2) / polynomial(gold_price['Year']))
    chi_squared_values[order] = chi_squared

    # Plot the fitted curve (original data is plotted later)
    plt.plot(x_values, y_values, color='red', label=f'Polynomial Fit (order {order})')

    return polynomial, covariance
# --- FUNCTION DEFINITION ENDS HERE ---

# Print to verify the data size before fitting polynomials
print(f"Total rows: {len(gold_price)}")

# Polynomial fits: orders 1 to 6 are always safe if you have enough data.
for order in range(1, 7):
    polynomial_fit, covariance = n_polynomial_fit(order)

# For higher orders, use try/except to avoid program crash on error
for order in range(7, 10):
    try:
        polynomial_fit, covariance = n_polynomial_fit(order)
    except ValueError as e:
        print(e)

# Plot gold price datapoints & polynomial fits
plt.scatter(
    gold_price['Year'],
    gold_price['Price'],
    label='Original Data',
    color='blue',
    s=10
)
plt.xlabel('Year')
plt.ylabel('Price per kg of Gold (USD)')
plt.title('Gold Price Forecasting using Polynomial Fitting')
plt.legend()
plt.show()

# Plot chi squared values for different polynomial orders
plt.plot(
    list(chi_squared_values.keys()),
    list(chi_squared_values.values()),
    marker='o',
    color='green'
)
plt.xlabel('Polynomial Order')
plt.ylabel('Chi Squared Value')
plt.title('Chi Squared Values for Different Polynomial Orders')
plt.show()

# Print final polynomial fit (the last one successfully fitted in the loop)
print(polynomial_fit)
