# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # Syntax error: missing parentheses, to call print need in form print()
print("\n") # Syntax error: Incorrect indentation used. Missing parentheses.

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax error: Incorrect indentation.
age_Str = ("24 years old")  # Logic error: Changed from '==' to '=' for assignment. Syntax error: Incorrect indentation used
numeric_part = age_Str.split()[0]
age = int(numeric_part)  # Runtime error - Value error: String contains characters. Cannot extract the number from a string conatining characters.
print(f"I'm {str(age)} years old.")  # Runtime error- Type error: Cannot concatenate string with integer. 

# Variables declaring additional years and printing the total years of age
# Syntax error: Incorrect indentation. 
years_from_now = 3  # Type error: should be assigned as an integer instead of a string
additional_months = 6  # Logical error: omission of additional months in the calculation of total number of months 
total_years = age + years_from_now  # Runtime error - Type error: cannot concatenate string with integer

print(f"The total number of years:{total_years}")  # Runtime error -Type error: Cannot concatenate string with integer

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + additional_months  # Runtime error - Name error: Variable 'total' is not defined.
# Logical error: Number of additional months needs to be added to total_months
print(f"In 3 years and 6 months, I'll be {total_months} months old")  # Runtime error - Type error: Cannot concatenate string with integer

# HINT, 330 months is the correct answer