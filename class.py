class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def greet(self):
    #     print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating multiple objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# Calling the greet method for each object
# person1.greet()
# person2.greet()
print(f"name: {person3.name}")