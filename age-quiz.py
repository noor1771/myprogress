#T03 Control Structures - If, Elif, Else and the Boolean Data Type
#Practical Task 1

def get_user_age():
    while True:
        try:
            age = int(input("Insert age here: "))
            return age
        except ValueError:
            print("Please enter a valid integer for age.")

age = get_user_age()

#Using the input command the user is asked to insert their age. The user's age will be stored as a string in the variable 'age' as an integer.
age = int(input("Insert age here "))
#The user will see a different message depending on the age inputed.
if age > 100:
    print("Sorry you're dead.")  #If their age is greater than 100, they will see "Sorry you're dead." as an output.
elif age >= 65:
    print("Enjoy your retirement!") #If their age is greater than or equal to 65, they will see "Enjoy your retirement!"
elif age >= 40:
    print("You're over the hill") #If their age is greater than or equal to 40, they will see "You're over the hill"
elif age == 21:
    print("Congrats on your 21st!") #If their age is 21, they will see "Congrats on your 21st!"
elif age < 13: 
    print("You qualify for the kiddie discount.")#If their age is less than 13, they will see "You qualify for the kiddie discount."
else: 
    print("Age is but a number.") #for all other ages they will see "Age is but a number" as an output.
