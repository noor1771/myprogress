#Challenge 2

#Prompt the user to input the name of their favourite restaraunt 
#Store input in variable 'string_fav'
string_fav = input('Enter the name of your favourite restaraunt: ')

#Prompt the user to input the name of their favourite number
#Store input in variable 'int_fav' as integer
int_fav = int(input('Enter your favourite whole number: '))

#print inputs on seperate lines
print('Favourite Resaraunt:',string_fav)
print('Favourite number:',int_fav)

string_fav = int(string_fav)
#This command will not execute because a string is a bunch of characters and you cannot convert a bunch of characters to a whole numer
#Only floats can be cast to inetegers because it is simply rounding a decimal number to a whole number
#Strings are not numbers
