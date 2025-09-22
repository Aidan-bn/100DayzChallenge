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