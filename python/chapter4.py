is_desert = True
print(type(is_desert))
b = bool(0.00)
c = bool(-1)
d = bool("")
print(b, c, d)
# print(bool(input()))
is_on = True
print(float(is_on), str(is_on), int(is_on))
v = 4
print(v < 4.0)
y = 'dog'
print(y > 'a')
num = -10
if num < 0:
    num = 25
if num < 100:
    num = num + 50

print(num)

score = int(input('Enter a score: '))
if score < 30:
    print('The entered value is minimum')
elif score == 40:
    print('The value is exactly 40')
print('The value is greater than 50')

day = 'saturday'
mood = input('Enter your mood: ')
if mood == 'blue':
    print('The day is Monday')
elif mood == 'red':
    print('The day is friday')


attendees = 350
rooms = 1

if attendees <= 100:
    rooms += 3
if attendees <= 200:
    rooms += 7
elif attendees <= 400:
    rooms += 14
else:
    print('Confused')
print('Number of rooms are: ', rooms)

hour = 12
if hour < 8:
    print("Too early")
elif hour < 12:
    print("Good morning")
elif hour < 13:
    print("Lunchtime")
elif hour < 17:
    print("Good afternoon")
else:
    print("Too late")

pen = input('Enter your choise: ')
user = input('Enter user name')

if (pen == 'cello'):
    if(user == 'Aidan'):
        print('Hand writting should be awesome')
    else:
        print('I am not sure ')
else:
    print('End of executiosion')
        
f = 1
g = 1
print (f, end = ' ')
while g < 20:
    print(g, '\n', end = " ")
    temp = f
    f = g
    g = temp + g
    
o = 1

while o < 10:
    if (o % 2 == 1):
        print( o, end=' ')
    o += 1
    
# Write a program that takes user inputs in a while loop until the user enters "begin". Test the code with
# the given input values to check that the loop does not terminate until the input is "begin". Once the input
# "begin" is received, print "The while loop condition has been met."

while True:
    userInput = input('Enter your input: ')
    if userInput == 'begin':
        print('The while loop condition has met')
        break
# Write a program that reads two integer values, n1 and n2. Use a while loop to calculate the sum of odd
# numbers between n1 and n2 (inclusive of n1 and n2). Remember, a number is odd if number % 2 != 0.

n1 = int(input('Enter the lowest number: '))
n2 = int(input('Enter the highest number: '))
numbers = []

total = 0
while n2 > n1:
    n1 +=1
    total += n1
    print(total)
