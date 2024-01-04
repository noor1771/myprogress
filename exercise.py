# Display Fibonacci series up to 10 terms
##a = 0
#b = 1
#sum = 0 

#for i in range(0,10,1):
    #print(a, end=" ")
    #sum = a + b 
    #a = b
    #b = sum
#print()

#Exercise 15: Use a loop to display elements from a given list present at odd index positions

#my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#or i in range(len(my_list)):
   # if i % 2 != 0:
       # print(my_list[i], end=" ")
#print()

#This code is inefficent
#for i in my_list[1::2]: #slicing, start at 1, til the end, ste of 2
    ####print(i, end=" ") #This constructs a loop that iterates through each element obtained from the slicing operation (my_list[1::2]) and 
    #assigns each element to the variable i.
#print()

#Exercise 16: Calculate the cube of all numbers from 1 to a given number

#cube_number = int(input("Input number: "))

#for i in range(cube_number):
    ##cube = pow(i,3)
    #print(f"Current Number is : {i} and the cube is {cube}")


# Enumerate practice:

word = ["hello","me","hello","mee"]


for i , element in enumerate(word, start=1):
    print(i, element)

holla = 'hu mu huf'
hollaa = holla.replace(" ","")
print(hollaa)

