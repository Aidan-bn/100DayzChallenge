def print_phone_num():
    print('Phone: (', 864, ')', 555, '-', '0199')

print_phone_num()

# Write a function, concessions(), that prints the food and drink options at a cinema.
# Given:

def concessions():
    print('Food/Drink Options:')
    print('Popcorn: $8 - 10')
    print('Candy: $3 - 8')
    print('Soft drink: $5 - 7')

concessions()

# Write an updated function, terms(), that asks the user to accept the terms and conditions, reads in Y/N,
# and outputs a response by calling accepted() or rejected(). accepted() prints "Thank you for
# accepting the terms." and rejected() prints "You have rejected the terms. Thank you.".

def accepted():
    print('Thank you for accepting the terms')

def rejected():
    print('You have rejected the terms. Thank you')
    
def terms():
    result = input('Are accepting the terms and condition?: ')
    if (result == 'Y'):
        accepted()
    elif(result == 'N'):
        rejected()
    else:
        print('You entered the incorrect answer')
terms()

def print_welcome(name):
    print(f'Welcome: {name}')
    
username = input('Enter new username: ')

print_welcome(username)

# Write a function, print_scores(), that takes in a list of test scores and a number representing how many
# points to add. For each score, print the original score and the sum of the score and bonus. Make sure not to
# change the list.
# Given function call:


def print_scores(a, b):
    for i in a:
        print(i, 'The new value of scorei', i + b)

print_scores([67, 68, 72, 71, 69], 10)