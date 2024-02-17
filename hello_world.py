#TO1 - Your first computer program and using variables
#Practical Task 1 

#User is asked to insert name. Input command is used to allow the user to do this.
#Their input is stored as a string in the variable 'name'
name = input("Insert your name here ")
#print function displays users input 
print(name)

#User is asked to insert their age.
try:
    age = int(input("Insert your age here: "))
except ValueError:
    print("Please enter a numeric value for age.")
print(age)


print('Hello World')
