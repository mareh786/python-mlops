# Object-Oriented Programming (OOP) in Python

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects**. An object is an instance of a class and contains both **data (attributes)** and **behavior (methods)**.

### Advantages

- Code Reusability
- Better Organization
- Easier Maintenance
- Modularity
- Scalability
- Real-world Modeling

---

# Class

A **class** is a blueprint for creating objects.

### Syntax

```python
class Student:
    pass
```

Example

```python
class Student:
    name = "Adil"

print(Student.name)
```

Output

```
Adil
```

---

# Object

An **object** is an instance of a class.

```python
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))
```

Output

```
<class '__main__.Student'>
```

Each object gets its own identity in memory.

---

# Class Namespace

The namespace of a class stores all variables and methods defined inside it.

```python
class Student:
    school = "ABC School"

    def greet(self):
        print("Hello")
```

Contents of namespace

```python
print(Student.__dict__)
```

Contains

- class variables
- methods
- built-in attributes

---

# Object Namespace

Every object has its own namespace.

```python
class Student:
    school = "ABC"

s1 = Student()
s2 = Student()

s1.name = "Adil"
s2.name = "Rahul"
```

Here,

```
s1.__dict__
```

```
{'name': 'Adil'}
```

```
s2.__dict__
```

```
{'name': 'Rahul'}
```

Each object stores only its own attributes.

---

# Attribute Shadowing

When an instance attribute has the same name as a class attribute, the instance attribute hides the class attribute.

```python
class Student:
    school = "ABC"

s = Student()

print(s.school)

s.school = "XYZ"

print(s.school)
print(Student.school)
```

Output

```
ABC
XYZ
ABC
```

The class variable remains unchanged.

---

# self Argument

`self` represents the current object.

Python automatically passes the object as the first argument.

```python
class Student:

    def display(self):
        print("Hello")
```

Internally,

```python
s.display()
```

is equivalent to

```python
Student.display(s)
```

Without `self`, an instance method cannot access object attributes.

---

# Constructor (__init__)

The constructor initializes an object when it is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Creating object

```python
s = Student("Adil", 23)
```

Output

```
Object initialized automatically.
```

---

# Inheritance

Inheritance allows one class to reuse properties of another.

```python
class Animal:

    def sound(self):
        print("Some sound")

class Dog(Animal):

    def bark(self):
        print("Bark")
```

Usage

```python
d = Dog()

d.sound()
d.bark()
```

Advantages

- Code Reuse
- Easy Extension
- Better Organization

---

# Composition

Composition means one class contains another class as an object.

Example

```python
class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car Moving")
```

Composition represents a **HAS-A** relationship.

Example

```
Car HAS-A Engine
```

Inheritance represents an **IS-A** relationship.

Example

```
Dog IS-A Animal
```

---

# Three Ways to Access Base Class

## 1. Using Parent Class Name

```python
class Parent:

    def display(self):
        print("Parent")

class Child(Parent):

    def show(self):
        Parent.display(self)
```

---

## 2. Using super()

```python
class Parent:

    def display(self):
        print("Parent")

class Child(Parent):

    def display(self):
        super().display()
```

Recommended approach.

---

## 3. Using Child Object

Inherited methods are directly available.

```python
class Parent:

    def display(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()

c.display()
```

---

# Method Resolution Order (MRO)

MRO decides the order in which Python searches for methods during inheritance.

```python
class A:

    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

c = C()

c.show()
```

Search order

```
C
↓

B
↓

A
↓

object
```

View MRO

```python
print(C.mro())
```

Output

```
[C, B, A, object]
```

Python uses the **C3 Linearization Algorithm** for MRO.

---

# Static Methods

Static methods belong to the class but do not use object or class data.

Decorator

```python
@staticmethod
```

Example

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage

```python
Math.add(2,3)
```

Static methods do not receive

- self
- cls

Use when utility logic doesn't depend on instance or class state.

---

# Class Method vs Static Method

## Class Method

Uses

```python
@classmethod
```

Receives

```python
cls
```

Example

```python
class Student:

    school = "ABC"

    @classmethod
    def get_school(cls):
        return cls.school
```

---

## Static Method

Uses

```python
@staticmethod
```

Example

```python
class Math:

    @staticmethod
    def square(x):
        return x*x
```

### Comparison

| Feature | Class Method | Static Method |
|----------|--------------|---------------|
| Decorator | @classmethod | @staticmethod |
| First Argument | cls | None |
| Access Class Variables | Yes | No |
| Access Instance Variables | No | No |
| Can Modify Class State | Yes | No |
| Utility Function | No | Yes |

---

# Property Decorator

The `@property` decorator allows a method to be accessed like an attribute.

Without property

```python
person.get_name()
```

With property

```python
person.name
```

Example

```python
class Student:

    def __init__(self):
        self._name = "Adil"

    @property
    def name(self):
        return self._name
```

Usage

```python
s = Student()

print(s.name)
```

Output

```
Adil
```

Benefits

- Cleaner syntax
- Data encapsulation
- Validation support

---

# Getter and Setter

Getter returns a value.

Setter updates a value with validation.

Example

```python
class Student:

    def __init__(self):
        self._age = 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Usage

```python
s = Student()

print(s.age)

s.age = 25

print(s.age)
```

Output

```
18
25
```

Invalid value

```python
s.age = -5
```

Output

```
ValueError: Age cannot be negative
```

---

# Summary

| Topic | Purpose |
|---------|----------|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Namespace | Storage of variables and methods |
| Attribute Shadowing | Instance attribute hides class attribute |
| self | Refers to current object |
| Constructor | Initializes object |
| Inheritance | Reuse existing class |
| Composition | HAS-A relationship |
| Base Class Access | Parent class methods access |
| MRO | Defines method lookup order |
| Static Method | Utility function |
| Class Method | Operates on class |
| Property | Access method as attribute |
| Getter | Read value |
| Setter | Validate and modify value |

---

# Key Takeaways

- Everything in Python is an object.
- A class is a blueprint; an object is its instance.
- `self` refers to the current object.
- `__init__()` initializes objects automatically.
- Inheritance models **IS-A** relationships.
- Composition models **HAS-A** relationships.
- Prefer `super()` when calling parent class methods.
- Python uses MRO to resolve inherited methods.
- Use `@staticmethod` for utility functions.
- Use `@classmethod` when working with class-level data.
- Use `@property` to expose methods like attributes.
- Use getters and setters to control access and validate data.
