my_list = [2, 3, 5, 7, 9]
for e in my_list:
    print(e, end='=')
    print(e, end='=')
    
for i in range(0, len(my_list)):
    print(i, end='|')

for i in range(0, len(my_list), 2):
    print(my_list[i], end=' * ')

items = [12, 3, 25, 16, -4, 9]
items.sort(reverse=True)
print(sorted(items))
items.reverse()
print(items)
print(sum(items))
print(max(items))

mat = [[17, 4, 5], [3, 9, 6], [1, 3, 8]]
print(mat[1][2])

for row in mat:
    for num in row:
        print(num, end=' ')
    print()

a_list = [1, 2, 3, 4, 5]
b_list = [i+2 for i in a_list]
print(b_list)

new_list = [i//3 for i in range(1, 15, 3)]
print(new_list)

# comprehension list it filter items in a list
my_mentioned = [21, -1, 50, 9, -20, 300, -50]
my_mentioned = [m for m in my_mentioned if m < 0]
print(my_mentioned)

my_string = 'This is a home'
new_list = [a for a in my_string if a in my_string]
print(new_list)

# Write a program that selects words that begin with an "A" in the given list. Make sure the new list is then
# sorted in dictionary order. Finally, print the new sorted list.

begin_with_A = ['Aborder', 'Sony', 'Philips', 'Abuja']
begin_with_A = [a for a in begin_with_A if a[0] == 'A']
begin_with_A.append('Gidan')
print(begin_with_A)
begin_with_A.remove('Abuja')
print(begin_with_A)
begin_with_A.pop()
print(begin_with_A)
