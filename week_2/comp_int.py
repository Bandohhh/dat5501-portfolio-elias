import math

def compound_interest(principal, rate, time):
    """
    Calculate the compound interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in decimal).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The amount of money accumulated after n years, including interest.
    """
    amount = principal * (1 + rate) ** time
    return amount

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal): "))
time = int(input("Enter the time in years: "))
total_amount = compound_interest(principal, rate, time)
for x in range(1, time + 1):
    yearly_amount = compound_interest(principal, rate, x)
    print(f"Amount after year {x}: {yearly_amount:.2f}")
print(f"The total amount after {time} years is: {total_amount:.2f}")

def investment_double_time(principal, rate):
    """
    Calculate the time required for an investment to double.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in decimal).

    Returns:
    float: The time in years required for the investment to double.
    """
    time = (math.log(2)) / (math.log(1 + rate))
    return time

doubled_amount = investment_double_time(principal, rate)
print(f"The time required for the investment to double is: {doubled_amount:.2f} years") 