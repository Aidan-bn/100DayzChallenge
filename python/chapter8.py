name = 'Juakali'
print(name[-2])

time_string = "13:46"

minutes = time_string[3:5]
hours = time_string[:2]

print(hours, minutes)

location = 'classroom'
print(location[-3:-1])

text = 'arbitrary'
print('ab' in text)
print('' in 'string')

for t in text:
    print(t, end = "")
    
count = 0
for c in 'abca':
    if c == 'a':
        count +=1
        print(count)
print(text.count('a'))
print(text.count('x'))

print('banana'.find('c'))
print('banana'.index('n'))

sentence = 'This is a sentence'
index = sentence.index(" ")
print(sentence[:index])

word = "Dear {}, I'd like to take a {} course with Prof {} "
print(word.format("John", "Programming", "Pottery"))

print("{} : {}".format("One", "1"))

s = "Weather in {season} is {temperature}."
print(s.format(season = "summer", temperature = "hot"))
greeting = 'Hi'
name = 'Jess'
print('{greeting} {name}'.format(greeting = greeting, name = name))

template1 = "{0} {0} {1}"
template2 = "{0} {1} {1} {0}"

print(template1.format("very", "cold"))
print(template2.format("very", "cold"))

template = "{hex:<7}{name:<5}"
print(template.format(hex = "#FF0000", name = "Red"))

template = "{hex:>7}{name:>5}"
print(template.format(hex = "#FF0000", name = "Red"))

template = "{hex:^7}{name:^5}"
print(template.format(hex = "#FF0000", name = "Red"))

temp = "{name:<12}"
temp_name = temp.format(name = "Alicyeu")
print(len(temp_name))

temp1 = "{greeting:<6}"
formated_temp1 = temp1.format(greeting = "Hello")
print(formated_temp1[0])

temp2 = "{:5}"
print(temp2.format("123456789"))

print("1*2*3*".split('*'))
print("a year includes 12 months".split())

s = """This is a test"""
out = s.split()
print(out)
print("".join(["This", "is", "great"]))