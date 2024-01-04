# T05 - Capstone Project

import math
# Display options for the user to choose between investment and bond calculations

while True:
    user_selection = ("investment - to calculate the amount of interest you'll earn on your investment \n")
    user_selection += ("bond - to calculate the amount you'll have to pay on a home loan \n")
    user_selection += ("Enter either 'investment' or 'bond' from the menu above to proceed: ")
# Ask the user to input their choice: 'investment' or 'bond'
    selection = input(user_selection).strip().lower()  # Normalize the input by converting to lowercase and removing leading/trailing spaces

# Validate user input, allowing for different capitalizations
    if selection == 'investment' or selection == 'bond':
        print("Proceed.")
        break
    else:
        print("Invalid selection.")

# Based on user choice, perform calculations for investment or bond
if selection == "investment":
    # Gather input for investment calculation: deposited money, interest rate, investment period, and interest type
    money_deposited = float(input("Enter amount of money you are depositing in: £ "))
    interest_rate = float(input("Enter interest rate percentage number: "))
    years_invested = float(input("Enter number of years you plan on investing for: "))
    interest = input("Enter either 'simple' for simple interest or 'compound' for compound interest: ")
    interest_decimal = interest_rate/100

    # Calculate investment value based on chosen interest type: simple or compound
    if interest.strip().lower() == "simple":
        simple_interest_total = money_deposited * (1 + interest_decimal * years_invested)
        print("Total investmet value at end of investment period = £  ", round(simple_interest_total, 2))
    elif interest.strip().lower() == "compound":
        compound_interest_total = money_deposited * math.pow((1 + interest_decimal), years_invested)
        print("Total investment value at end of investment period = £ ", round(compound_interest_total, 2))

else:
    if selection == "bond":
        # Gather input for bond repayment calculation: present value, annual interest rate, repayment period
        present_value = float(input("Enter the present value of the house: £ "))
        annual_rate = float(input("Enter annual interest rate percentage number: "))
        monthly_rate = (annual_rate/100)/12
        repayment_months = float(input("Enter the number of months you plan to repay the bond for: "))

        # Calculate bond repayment amount
        bond_repayment = (monthly_rate * present_value)/(1 - (1 + monthly_rate) ** (-repayment_months))
        print("Repayment = £", round(bond_repayment, 2))
