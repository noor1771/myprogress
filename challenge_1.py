#Challenge 1

#Prompt user to enter the lengths of all three sides of a triangle in centimetres
#Store lengths as floats in variables
import math

side_1 = float(input('Enter length of first side of the traingle in cm: '))
side_2 = float(input('Enter length of second side of the traingle in cm: '))
side_3 = float(input('Enter length of third side of the traingle in cm: '))

#Sum all sides of traingle and divide by 2
#Store this answer in variable 'sum_2'
sum_2 = (side_1 + side_2  + side_3)/2

#Calculate area of the traingle using the inputed lengths and sum divided by 2 'sum_2'
#Store area as a variable

triangle_area = math.sqrt((sum_2*(sum_2 - side_1))*(sum_2 - side_2)* (sum_2 - side_3))
print('Traingle Area =', round(triangle_area,2), 'cm²')
