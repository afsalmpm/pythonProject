# Super class and subclasses
# or Prent class or child class
# It is like super set sub set
# Inheritance subclass will inherit super class "methods" and "attributes"
# Attributes are defined in classes by variables. ...
# Because each instance of a class can have different values for its variables,
# these variables are often called instance variables.

class Pet: # Pet is a super class or parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f" I am {self.name} and {age} years old")

    def speak(self):
        print("I don't know what to speak")


class Cat(Pet):  # Putting Pet in bracket will result in inheritance of pet class qualities
    def speak(self): # Dog and Cat are subclasses
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bow bow")


class Fish(Pet):
    def swim(self):
        print("shwi shwi shwi")



Dog1 = Dog("Shivaji", 18)
Cat1 = Cat("Mullu",22)
Dog1.speak()
Cat1.speak()
Fish1 = Fish("bubloo", 10)
Fish1.speak()

