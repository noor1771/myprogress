# T02 - The String and Numerical Data Type
# Practical Task 2

# Prompt the user to enter their sentence
# Store the setence in variable 'str_manip'
str_manip = input("Enter sentence here ")
num_characters = len(str_manip)
# ouput the number of characters
print('Number of characters =', num_characters)
# Print the number of characters
num_words = len(str_manip.split())
# ouput the number of words
print('Number of words =', num_words)
# Print the number of words

last_letter = str_manip[-1]
str_manip_at = str_manip.replace(last_letter, "@")
# replace every occurence of the last_letter in str_manip with an '@'.


print(str_manip[-1:-4:-1])
# print the last 3 characters in strip str_manip backwards

# Concatenate first three characters and last two characters
# of str_manip to create 5 letter words
# Store five letter in variable 'alien word'
first_three = str_manip[0:3]
last_two = str_manip[-2:]
alien_word = "{}{}".format(first_three, last_two)
print('Alien word:', alien_word)
