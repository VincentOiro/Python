# This is an example of object-oriented programming in Python

class Person:
    # This is a class definition for a Person

    def __init__(self, name, age, address):
        # This is the constructor method that is called when a new object is created
        # It initializes the object with the given values of name, age, and address
        self.name = name  # This sets the name attribute of the object
        self.age = age    # This sets the age attribute of the object
        self.address = address  # This sets the address attribute of the object

    def greet(self):
        # This is a method that prints a greeting message
        print(f"Hello, I am {self.name} and I am {self.age} years old!")

    def get_age(self):
        # This is a method that returns the value of the age attribute
        return self.age

# Create a new object of the Person class
p = Person("John Doe", 30, "123 Main St.")

# Call the greet method on the object
p.greet()  # Output: Hello, I am John Doe and I am 30 years old!

# Call the get_age method on the object
print(p.get_age())  # Output: 30