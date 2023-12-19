"""
Compulsory Task 2: 
------------------


1. Take user inputs that take in name, age, hair colour, eye colour of a person
2. Create an Adult class with the following methods and attributes:
    --- Attributes: name, age, hair_colour, eye_colour
    --- Methods: can_drive that prints the name of the person and that they are old enough to drive
3. Create a subclass of the Adult class called Child which inherits all attributes but overwrites can_drive method
    --- to print out the name and that they are too young to drive 
4. Create logic to determine if the person is 18 or over and create an instance of the adult class if this is true
    Otherwise create an instance of the child class. Once the object has been created, call the can_drive method to print out if they are old enough to drive or not
"""
class InvalidInputError(Exception):
    pass


class Adult:
    '''
    This class creates the Adult blueprint with the attributes of name, age, hair colour, eye colour and the method of 
    >>>> can_drive which states that the adults can drive 
    '''
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self, name):
        print(f"{self.name}: They are old enough to drive")
    

class Child(Adult):
    '''
    This class inherits all traits from the Adult class
    It overwrites the can_drive method to print the name and 'They are not old enough to drive' 
    '''
    def can_drive(self, name):
        print(f"{self.name}: They are not old enough to drive")


# Defines the number of attemps that are allowed before failing
n_attempts = 5

for attempts in range(n_attempts):
    try:
        age = int(input("Please enter the age of the person: ").strip()) # This strips out all spaces
    except ValueError:
        raise InvalidInputError("This is not an integer")
    break

name = input('Please enter the name of the person: ')
hair_colour = input('Please enter the hair colour of the person: ')
eye_colour = input('Please enter the eye colour of the person: ')

if age >= 18:
    person_1 = Adult(name, age, hair_colour, eye_colour) # This creates an instantiation of the Adult class
else:
    person_1 = Child(name, age, hair_colour, eye_colour) # This creates an instantiation of the Child class

person_1.can_drive(name)
