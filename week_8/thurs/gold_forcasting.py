import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#Dictionary to store chi squared values for different polynomial orders
chi_squared_values = {}

#Load as the CSV
gold_price = pd.read_csv('week_8/thurs/price-per-kg-of-gold.csv')

#drop columns we don't need
columns_to_drop = ['Entity', 'Code']
gold_price = gold_price.drop(columns=columns_to_drop)

pd.set_option('display.max_rows', None)  #Display all rows

#change the name of the Gold (New York Market Price) (Laurence & Williamson (2017)) to Price
gold_price = gold_price.rename(columns={'Gold (New York Market Price) (Laurence & Williamson (2017))': 'Price'})

#create a sub sample of the last 100 years without data from the last 10 years 
gold_price = gold_price[(gold_price['Year'] <= 2015) & (gold_price['Year'] >= 1915)]

def n_polynomial_fit(order):
    #Fit a polynomial of given order to the sample data 
    coefficients = np.polyfit(gold_price['Year'], gold_price['Price'], order)
    polynomial = np.poly1d(coefficients)

    #Generate x values for plotting the fitted Curve
    x_values = np.linspace(gold_price['Year'].min(), gold_price['Year'].max(), 100)
    y_values = polynomial(x_values)
    
    #Calculate chi squared value for the fit
    residuals = gold_price['Price'] - polynomial(gold_price['Year'])
    chi_squared = np.sum((residuals ** 2) / polynomial(gold_price['Year']))
    chi_squared_values[order] = chi_squared
 
    #Plot the original data and fitted curve 
    plt.plot(x_values, y_values, color ='red', label=f'Polynomial Fit (order {order})')


    return polynomial

#example usage : polyomial fit of order 3


polynomial_fit = n_polynomial_fit(1)
polynomial_fit = n_polynomial_fit(2)
polynomial_fit = n_polynomial_fit(3)
polynomial_fit = n_polynomial_fit(4)

polynomial_fit = n_polynomial_fit(5)
polynomial_fit = n_polynomial_fit(6)
polynomial_fit = n_polynomial_fit(7)
polynomial_fit = n_polynomial_fit(8)
polynomial_fit = n_polynomial_fit(9)


#plot gold price data points & polynomial fit
plt.scatter(gold_price['Year'], gold_price['Price'], label='Original Data', color='blue', s=10)
plt.xlabel('Year')
plt.ylabel('Price per kg of Gold (USD)')
plt.title('Gold Price Forecasting using Polynomial Fitting')
plt.legend()
plt.show()

#plot chi squared values for different polynomial orders
plt.plot(chi_squared_values.keys(), chi_squared_values.values(), marker='o', color='green')
plt.xlabel('Polynomial Order')
plt.ylabel('Chi Squared Value')
plt.title('Chi Squared Values for Different Polynomial Orders')
plt.show()

print(polynomial_fit)








