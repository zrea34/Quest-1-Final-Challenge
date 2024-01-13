from calculator import calc_driver as calc
import utils.hello.example as ex
from pydantic import BaseModel

groceries = ["milk", "eggs", "bread", "butter", "bacon"]
'''
for i in range(len(groceries)):
    groceries[i] = groceries[i] + "ay"

print(groceries)
'''


# dictionaries
'''
user_dictionary = {
    "zachh": "zach hope",
    "howie": "howie johnson"
}

username = input("add a username: ")
name = input("what is your full name? ")

user_dictionary[username] = name
print(user_dictionary[username])

search = input("search by username: ")
print(user_dictionary.get(search, "Value not found"))
'''

# functions

'''
def say_hello():
    print("hello")


say_hello()
'''


# write a function that returns the smallest number in a list

'''
def find_smallest(list):
    return min(list)


print(find_smallest([1,2,3,4,5,0]))
'''
# calls my calculator function
# calc()


class Product:
    # data, state
    price:  float
    name: str
    is_active: bool

    # behavior
    def set_price(self, price):
        # data validation
        if price < 0:
            self.price = 0
        self.price = price

    def get_price(self):
        return self.price

    # constructor: set intial values for object
    def __init__(self, name, price, is_active):
        self.name = name
        self.price = price
        self.is_active = is_active


# Constructors
tv = Product("TV", 500, True)


class Person(BaseModel):
    id: int
    name: str


customer = {
    'id': 1,
    'name': 'Zach'
}

# ** = unpacking
p = Person(**customer)
print(str(p.id) + " : " + p.name)
'''
# create a class that contains devs names, salary and language
class Developer():
    name: str
    salary: int
    language: str

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language


dev1 = Developer("John", 90000, "SQL")
dev2 = Developer("Jenna", 110000, "Java")
dev3 = Developer("Katherine", 95000, "Python")

devs = [dev1, dev2, dev3]

for i in range(len(devs)):
    print(devs[i].name + ": " + devs[i].language + " -- " + str(devs[i].salary))


# parent class
class Animal:
    weight: int
    name: str

    def speak(self):
        return "strange noise"


# Dog extends animal
class Dog(Animal):
    breed: str

    def play(self):
        print("playing")

    def speak(self):
        return "bark"


class Cat(Animal):
    def speak(self):
        return "meow"


list = [Dog(), Cat(), Dog(), Animal()]

for animal in list:
    print(animal.speak())
'''
