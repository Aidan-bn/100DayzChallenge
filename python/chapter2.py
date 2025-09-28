# Write a program that reads in two strings, str1 and str2, and an integer, count. Concatenate the two
# strings with a space in between and a newline ("\n") at the end. Print the resulting string count times.
str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
count = int(input('Enter the count'))
print('The first string entered was: ', str1, 'The second string entered was: ', str2, '\n And the count was: ', count )

# Complete the following steps to calculate a triangle's area, and print the result of each step. The area of a
# triangle is , where b is the base and h is the height.
# 1. Calculate the area of a triangle with base = 7 and height = 3.5.
# 2. Round the triangle's area to one decimal place.
# 3. Round the triangle's area to the nearest integer value
base = 7
height = 3.5
area = (base * height)/2
print('The are of a triangle is: ', round(area, 2))

# Write a program that (1) inputs the current time and estimated length of a trip, (2) calculates the time of
# arrival, and (3) outputs the results in hours and minutes. Your program should use the following prompts
# (user input in bold):
# time = int(input('Enter current time: '))
# distance = int(input('Enter estimated time of trip: '))
#arrival = distance/time
result_in_hours = (distance + time) // 60
result_in_minutes = (distance // time) * 60
print('The result in hours: ', result_in_hours)
print('The result in minutes: ', result_in_hours)

import math
print('The square root is: ', math.sqrt(36))
