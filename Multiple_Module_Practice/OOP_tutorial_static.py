
class Person:
    number_of_people = 0  # an attribute is always the same for all instances of Person

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    #Decorator (the yellow part)
    @classmethod  # this method is not specific to an instance but specific to the whole class
    def numberofpeople(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("jim")

print(Person.number_of_people)

# We call also change for the whole class
Person.number_of_people = 8

print(Person.number_of_people)
print(p1.numberofpeople())
p1.add_person()
print(p2.numberofpeople())
print(Person.numberofpeople())


# Static methods
# Organize functions into an object


class Math:
    @staticmethod  # means this class does not have access to an instance; they just store and perform certain functs
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")


print(Math.add5(10))
print(Math.add10(10))
Math.pr()
