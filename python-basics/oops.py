"""
Question 1

Create a Book class.

Requirements:
- title
- author
- price

Create two books and print all details.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("Python", "Guido", 500)
b2 = Book("DSA", "Aditya", 700)

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

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(self.brand, self.model, self.price)


mob1 = Mobile("Vivo", "V27", 33000)
mob2 = Mobile("Samsung", "S24", 60000)

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

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle

    def perimeter(self):
        perimeter_of_rectangle = 2 * (self.length + self.width)
        return perimeter_of_rectangle


rec1 = Rectangle(10, 5)

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

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False


s1 = Student("Adil", 35)

print(s1.is_pass())
