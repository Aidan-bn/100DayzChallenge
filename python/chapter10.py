encoding = {'a': 12, 'b': 24, 'A': 90}
print(type(encoding))
names = {'Aidan':1, 'Habayo':2, 'Juma':3, 'Lukas':4, 'Yakobo':5}
print(names)

fruits = {}
print(fruits)

listed = [('apple', 2), ('banana', 3), ('soda', 5), ('mnavu', 9) ]
my_list = dict(listed)
print(my_list)

short = dict({'a' : 1})
print(short)
print(my_list['banana'])
print(my_list.get('soda'))

members = { 'Jaya': 'Student', 'John': 'TA', 'Koku': 'Staff'}
print(members['Jaya'])
print(members.get('jaya', 'does not exist'))

print(members.values())
print(members.keys())
print(members.items())
print('original', members)
members['Habayo'] = 1
print(members)

members.update({'Jaya' : 'Student', 'Aidan' : 'Developer'})
print(members)

del members['Jaya']
print(members)
members['John'] = 'Driver'
print(members)

# Create a dictionary of cars step-by-step
# Follow the steps below to create a dictionary of cars and modify it step-by-step.
# 1. Create an empty dictionary.
# 2. Add a key-value pair of "Mustang": 10.
# 3. Add another key-value pair of "Volt": 3.
# 4. Print the dictionary.
# 5. Modify the value associated with key "Mustang" to be equal to 2.
cars = {}
cars.update({'Mustang' : 10})
cars.update({'Volt' : 3})
cars['Mustang'] = 2
del cars['Volt']
print(cars)

# conditional statement on dictionary
print(('John', 'Driver') in members.items()) #The output is True oFlse

# conditional on values or keys
print(cars['Mustang'] < 1)
print('John' in members.keys()) 
print('TA' in members.values())

# iterate over key value
zip_codes = {'Berkeley' : 47800, 'Santa Cruz' : 2310, 'Mountain View' : 94500}

for a, b in zip_codes.items():
    print(a, b)
    
for r in zip_codes.keys():
    print(r)

for x in zip_codes.values():
    print(x)

# Given a string value, calculate and print the number of occurrences of all characters using a dictionary.
# Input:
# string_value = "This is a string"
# Prints {"T": 1, "h": 1, "i": 3, "s": 3, " ": 3, "a": 1, "t": 1, "r": 1, "n": 1,
# "g": 1}




# Given a fruit_count dictionary that contains information about fruits and the count of each fruit,
# calculate the total number of fruits across all fruit types.
# Input:

fruit_count = {"banana": 2, "orange": 5, "peach": 5}
for q in fruit_count.values():
    print(q)

company_org_chart = {
    'Marketing': {
        'ID123': 'Me Tuber'
    },
    'Sales': {
        'ID213': 'Bob Makani',
        'ID321': 'Junior Mabula'
    },
    'Engineering': {
        'ID001': 'Baziza Bazizane'
    }
}

print(company_org_chart['Engineering']['ID001'])

# Given a list, create a dictionary with two keys, "even" and "odd". The values associated with each key must
# be the list of corresponding even and odd values in the given list.
# Input:
input_list = [3, 5, 6, 1]

