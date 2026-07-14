"""
Question 1

Create a Book class.

Requirements:
- title
- author
- price

Create two books and print all details.
"""

# Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


# Creating book objects
b1 = Book("Python", "Guido", 500)
b2 = Book("DSA", "Aditya", 700)

# Printing book details
print(b1.title, b1.author, b1.price)
print(b2.title, b2.author, b2.price)


"""
Question 2

Create a Mobile class.

Requirements:
- brand
- model
- price

Add a method:
display_details()

that prints all information.
"""

# Mobile class
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Display mobile details
    def display_details(self):
        print(self.brand, self.model, self.price)


# Creating mobile objects
mob1 = Mobile("Vivo", "V27", 33000)
mob2 = Mobile("Samsung", "S24", 60000)

# Calling display method
mob1.display_details()
mob2.display_details()


"""
Question 3

Create a Rectangle class.

Constructor should accept:
- length
- width

Methods:
- area()
- perimeter()

Example:
r = Rectangle(10, 5)

print(r.area())
print(r.perimeter())
"""

# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate area
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle

    # Calculate perimeter
    def perimeter(self):
        perimeter_of_rectangle = 2 * (self.length + self.width)
        return perimeter_of_rectangle


# Creating rectangle object
rec1 = Rectangle(10, 5)

# Printing area and perimeter
print(rec1.area())
print(rec1.perimeter())


"""
Question 4

Create a Student class.

Attributes:
- name
- marks

Method:
- is_pass()

Returns:
- True if marks >= 40
- False otherwise
"""

# Student class
class Student:
    pass
