# class Cat:
#     def __init__ (self):
#         self.name = 'Kitty'
#         self.breed = 'Domestic short hair'
#         self.age = 1
#     def print_info(self):
#         print(self.name, 'is a', self.age, 'yr old', self.breed)
        
# pet_1 = Cat('Luio', 'Black', 12)
# pet_2 = Cat()
    
class Cat:
    def __init__(self):
        self.name = 'Kitty'
        self.breed = 'domestic short hair'
        self.age = 1
    def print_info(self):
        print(self.name, 'is a ', self.age, 'yr old', self.breed)

pet_1 = Cat()
pet_1.name = 'Abujadaf'
pet_1.breed = 'Kimburu'
pet_1.age = 12
print(pet_1.print_info())

# pet_2 = Cat()

# Write a class, FlightTicket, as described below. Default values follow the attributes. Then create a flight
# ticket and assign each instance attribute with values read from input.
# Instance attributes:
# • flight_num: 1
# • airport: JFK
# • gate: T1-1
# • time: 8:00
# • seat: 1A
# • passenger: unknown
# Class attributes:
# • airline: Oceanic Airlines
# • airline_code: OA
# Method:
# • __init__(): initializes the instance attributes
# • print_info(): prints ticket information (provided in template)
# Given input:
# 2121
# KEF
# D22B
# 11:45
# 12B
# Jules Laurent

class FlightTicket:
    def __init__(self):
        self.flight_num = 'flight_num'
        self.airport = 'airport'
        self.gate = 'gate'
        self.time = 'time'
        self.seat = 'seat'
        self.passenger = 'passenger'
    def print_info(self):
        print('Passenger', self.passenger, 'departs on flight # ', self.flight_num, 'at', self.time, 'from', self.airport, 'in', self.seat)

passenger_1 = FlightTicket()
# passenger_1.flight_num = input('flight_num: ')
# passenger_1.airport = input('airport: ' )
# passenger_1.gate = input('gate: ')
# passenger_1.time = input('time: ')
# passenger_1.seat = input('seat: ')
# passenger_1.passenger = input('passenger: ')

# print(passenger_1.print_info())

class Book:
    def __init__ (self):
        self.book_id = '5'
        self.book_author = 'Habayo'
        self.book_title = 'Marriage Wedding'
    def book_library(self):
       print('In our Library, the folloeing Book', self.book_title, 'written by', self.book_author, 'with an ID', self.book_id, 'is no longer available')

book_1 = Book()
# book_1.book_author = 'Aidan Banteze'
book_1.book_id = 'A12PL'
# book_1.book_title = 'The secret of marriage'
print(book_1.book_library())

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("That person's name is ", self.name)

first = Person('Aidan Banteze')
# first.name = 'Aidan Banteze'
print(first.introduce())

