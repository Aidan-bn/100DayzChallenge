str_var = "A string"

count = 0
for c in str_var:
    count += 1
    print(c, end = '*')
print(count)

# n1 = int(input('Enter the lowest number: '))
# n2 = int(input('Enter the highest number: '))

# while n2 > n1:
#     print(n1)
#     n1 +=1

# Write a program using a for loop that takes in a string as input and counts the number of spaces in the
# provided string. The program must print the number of spaces counted. Ex: If the input is "Hi everyone",
# the program outputs 1.

user_input = input('Enter your string: ')
total = 0
for empty in user_input:
    if empty == " ":
    # empty += 1
        total = total + empty.count(' ')
        print('Empty spaces in total are: ', total)

hour = 8
minute = 0
while hour <= 9:
    while minute <= 59:
        print(hour, ":", minute)
        minute += 30
    hour += 1
    minute = 0

numbers = [2, 5, 7, 11, 12]
for d in numbers:
    if d == 10:
        print("Found 10!")
        break
else:
    print("10 is not in the list.")

string_val = "Hello World"
for c in string_val:
    if c == " ":
        print('There is a space')
        break
else:
    print('There is no space')

r = 1
while True:
    if r%3 == 0 and r%5 == 0:
        print(r)
        break
    r +=1
    
    j = 1
    count = 0
    while True:
        if j % 2 == 0 or j % 2 == 0:
            count += 1
        if count >= 5:
            print(j)
            break
        j += 1



