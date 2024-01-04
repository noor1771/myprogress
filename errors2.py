# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # Syntax error: Lion is a string type and should be placed inside quotation marks either "Lion" or 'Lion'
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"  #Synatx error: Need to use proper string formatting with `.format()` method or f-strings
# full_spec = "This is a {0}. It is a {1} and it has {2} teeth".format(animal, animal_type, number_of_teeth)

print(full_spec)  # Syntax error: print statment missing parenthese
