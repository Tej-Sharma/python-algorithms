import random
import sys
import os

# LISTS
lists = [['hi', 1], 'hello', 2]
lists.append('namaste')

# Inserts an item BEFORE the given index
lists.insert(1, 'Pickle')
# Other features
lists.remove('Pickle') #remove an item
lists.sort()
lists.reverse() 
del lists[0] # delete an index
list2 = ['lol', 'mclol']
list3 = lists + list2


# TUPLES
tuple1 = (1, 2, 3, 4, 5)
listVer = list(tuple1)
backToTuple = tuple(listVer)
#len(tuple1) min(tuple1) max(tuple1)


# DICTIONARIES / HASH MAPS (note: can not be concatenated)
cities = {'New York': 'NY', 'Los Angeles': 'LA'}
cities['New York']
del cities['New York']
cities['New York'] = 'Swag City'
cities.keys()
cities.values()

# Advanced python dictionary: dict within dict with list value
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print 1
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print city

print 2
asia_cities = []
# .iteritems() is more efficient
for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city

# if : elif : else:
# and, or, not(age == 30), !=

#for loops
for i in range(0, 10):
    print(i, ' ', end="")
    
print('\n')

for i in lists:
    for y in lists:
        print(y)

randNumb = random.randrange(0, 100)

while(randNumb != 15):
    print(randNumb)
    randNumb = random.randrange(0, 100)
    
# also break and continue commands

# functions 
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

# Console I/O
print('what\'s your name?')
name = sys.stdin.readline()
print('Hello', name)


# Python String manipulation
long_string = "Hello bob"
long_string[:5] # 'Hello'
long_string[-3:] # 'bob'

txt = long_string
txt.capitalize()
txt.find('bob')
# All characters
txt.isalpha()
# All numbers
txt.isalnum()
len(txt)
txt.replace('bob', 'billy')
txt.strip()
txt.split(" ")
# String splicing
name_input = '$$$%%%%inputted_name%%%%$$$'
name_splice = name_input[:5]
# Custom printing
print('%c - character %s - string %d - number %.2f - decimal', % ('A', 'word', 1, 0.05))



# File OP

fileIO = open("text.txt", "ab+")
fileIO.write(bytes("Write me to the file!", "UTF-8"))
fileIO.close()

fileIO = open("text.txt", "r+")
fileText = fileIO.read()

# Delete file
os.remove("text.txt")



# OOB programming
# Taken from Mr. Banas' "Python In One video" for educational purposes
class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None
 
    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class

    # Multiple constructors are not allowed but can set default values
    def __init__(self, name="", height=0, weight=0, sound="generic meow"):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
 
    def set_name(self, name):
        self.__name = name
 
    def set_height(self, height):
        self.__height = height
 
    def set_weight(self, height):
        self.__height = height
 
    def set_sound(self, sound):
        self.__sound = sound
 
    def get_name(self):
        return self.__name
 
    def get_height(self):
        return str(self.__height)
 
    def get_weight(self):
        return str(self.__weight)
 
    def get_sound(self):
        return self.__sound
 
    def get_type(self):
        print("Animal")
 
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')
 
print(cat.toString())


class Cow(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Cow, self).__init__(name, height, weight sound)
    def set_owner(self, owner):
        self.__owner = owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        return self
    def toString(self):
        return "Dog go wooffff"
    # Method Overloading
    # By setting default value to "None" (don't require)
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sond())
        else:
            print(self.get_sound() * how_many)

spot = Dog("JOE", 53, 27, "Woof", "Bode")

