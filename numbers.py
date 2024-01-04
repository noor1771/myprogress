# T02 - The String and Numerical Data Type
# Practical Task 3

# Promp the user to input 3 integers.
# Store the first, second, and third number in variables as integers
first_number = int(input("Enter first integer "))
second_number = int(input("Enter second integer "))
third_number = int(input("Enter third integer "))

# Add up the first, second and third number
sums = first_number + second_number + third_number
print(f'The sum of all the numbers = {sums}')
# Print the sum of the three numbers

# Calculate the first number subtract the second number
first_minus_second = first_number - second_number  # Store answer in variable
print(f'The first number minus the second number = {first_minus_second}')
# Print answer

# Calculate third number multipled by the first number
third_times_first = third_number * first_number  # Store answer in variable
print(f'Third number multiplied by the first number = {third_times_first}')
# Print answer

# Divide the sum of all three numbers by the third number
sum_divide_third = sums / third_number  # Store answer in variable
print(f'Sum of all three numbers divided by third number = {sum_divide_third}')
# Print answer
