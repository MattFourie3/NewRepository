# Imports the math module
import math

# Input variable for user input for 'investment' or 'bond' stores in lower case
user_calc_choice = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment      - to calculate the amount of interest you'll earn on interest.
bond            - to calculate the amount you will have to pay on a home loan.

: """).lower()
# Checks user input for the 'investment' output
if user_calc_choice == "investment":
    # Different input variable types
    deposit_amount = float(input("Please enter in the amount you would like to deposit: "))
    interest_rate = float(input("Please enter the interest rate(do not add the '%' icon): "))
    years_investing = int(input("Please enter the number of years you plan on investing for: "))
    interest = input("Would you like the 'Simple' or 'Compound' interest: ").lower()
    # Variables of the formula to calculates the users interest based on their input
    simple_total = deposit_amount * (1 + (interest_rate / 100) * years_investing)
    compound_total = deposit_amount * math.pow((1 + (interest_rate / 100)), years_investing)
    # Checks if user input is 'simple' or 'compound' and print output based on input and rounds to 2 decimal places
    if interest == "simple":
        print(f"Simple Interest total: {round(simple_total, 2)}")
    elif interest == "compound":
        print(f"Compound Interest total: {round(compound_total, 2)}")
    else:
        pass
# Checks user input for the 'bond' output
elif user_calc_choice == "bond":
    house_value = float(input("What is the present value of the house: "))
    # Variable that get input from user then converts the interest into monthly interest rate
    interest_rate = float(input("Enter the interest rate(do not add the '%' icon): "))
    interest_rate = float(interest_rate) / 100 / 12
    num_months = float(input("Enter the number of months you plan to take to pay off the bond: "))
    # Variable for the formula to calculate monthly payments
    # Formula was not working using it directly form pdf - used below link to get formula
    # https://stackoverflow.com/questions/29804843/calculating-mortgage-interest-in-python
    repayment = house_value * (interest_rate * (1 + interest_rate) ** num_months) / ((1 + interest_rate) ** num_months - 1)
    # prints out calculated monthly payment and rounds to 2 decimal places
    print(f"Your monthly payment on this bond is: {round(repayment, 2)}")
    # If neither 'investment' or 'bond' is implemented, prints below message.
else:
    print("Sorry is not a valid input! Please type out 'investment' or 'bond'")
