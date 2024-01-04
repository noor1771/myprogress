# T04 Logical Programming
# Practical Task 1

# Ask the user for the time taken for swimming, cycling,and running in minutes.
# Convert the input times to floating-point numbers.

swimming_time = float(input('Swimming time in minutes: '))
cycling_time = float(input('Cycling time in minutes: '))
running_time = float(input('Running time in minutes: '))

# Calculate the total time by adding the times for swimming,cycling,and running
# Display the total time taken.
total_time = swimming_time + cycling_time + running_time
print(f'Total time: {total_time} minutes')

# Determine the type of award based on the total time:
# - If total time is between 0 and 100 minutes (inclusive), award Provincial Colours.
# - If total time is between 101 and 105 minutes (inclusive), award Provincial Half Colours.
# - If total time is between 106 and 110 minutes (inclusive), award Provincial Scroll.
# - Otherwise, display "No Award".


if 0 <= total_time <= 100:
    print('Award: Provincial Colours')
elif 101 <= total_time <= 105:
    print('Award: Provincial Half Colours')
elif 105 <= total_time <= 110:
    print('Award: Provincial Scroll')
else:
    print('No Award')
# Display the type of award or "No Award" based on the total time taken.
    