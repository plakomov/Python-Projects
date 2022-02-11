# Creating a class object in Python practice


# Notes:
# Always include  __init__  method with a self parameter inside
# You can use __init__ method to provide attributes to the classes

# Inheritance <- a class inherits the attributes and methods of another class

# Example:

class Pet:  # generalization
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):  # <--- (Pet) means the class Cat inherits the properties of Pet
    def __init__(self, name, age, color):  # need to include name and age
        super().__init__(name, age) # reference Pet class; we call the superclass and we need the parent initialization
        self.color = color

    def speak_(self):
        return print("Meaow")


class Dog(Pet):
    # def __init__(self, name, age):
    #   self.name = name
    #  self.age = age
    def speak_(self):
        return print("Bark")

# ct = Dog("tim", 59) # <- inherits all the attributes and methods of Pet
# ct.show()

