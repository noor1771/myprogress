# Calculate the radius and surface area of a cylindrical canister based on the given volume and height.

import math

# Erroneous Calculation Section

# Incorrectly calculated volume
volume_str = "0.5 L"
volume = float(volume_str.split()[0])  # Extract the volume as a float number

# User input for height of canister
height = float(input("Enter height of canister in meters: "))

# Incorrect calculation of radius due to a logical error (V = πr²h)
radius = volume / (height * math.pi)  # Incorrect formula for calculating radius
print(f"Radius of the cylindrical canister: {radius:.2f} m")

# Incorrectly calculated surface area based on flawed radius
# Equation for calculating the surface area of a cylinder: 2πrh + 2πr²
surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)

# Explanation of the logical error in radius calculation and its impact
print("The calculated radius is inaccurate due to the logical error in the formula.")
print("This impacts the surface area calculation resulting in an inaccurate surface area value.")
print(f"Surface Area of the cylindrical canister (based on flawed radius): {surface_area:.2f} m²\n")

# Correct Calculation Section

# Given volume and height in correct units
volume_str = "0.5 L"  # Representing volume in liters
volume = float(volume_str.split()[0])  # Extract the volume as a float number
height = float(input("Enter height of canister (in meters): "))  # User input for height in meters

# Calculating the radius based on the correct volume and height relationship (V = πr²h)
radius = math.sqrt(volume / (math.pi * height))  # Correct formula for calculating radius
print(f"Radius of the cylindrical canister: {radius:.2f} m")

# Calculating the surface area of the cylindrical canister
surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)

# Displaying the calculated surface area
print(f"Surface Area of the cylindrical canister: {surface_area:.2f} m²")
