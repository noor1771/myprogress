#TO1 - Your first computer program and using variables
#Practical Task 2

#Input command used to allow user to insert the following information 
#Name, Age, House number, Street name (in that order). This information will be stored as strings in variables shown below:

Name = input("Enter name here ")
Age = input("Enter age here ")
House_Number = input("Enter House Number here ")
Stree_Name = input("Enter Street Name here ")

#A single sentence containing these details will print out: This is {Name}. {Name} is {Age} years old and lives at house number {House_Number} on {Stree_Name}
print(f'This is {Name}. {Name} is {Age} years old and lives at house number {House_Number} on {Stree_Name}')