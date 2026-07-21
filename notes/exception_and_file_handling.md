# Exception Handling and File Handling in Python

## What is an Exception?

An **exception** is an event that interrupts the normal execution of a program. It usually occurs due to an error during runtime.

Examples:

- Dividing by zero
- Accessing an invalid list index
- Opening a non-existent file
- Converting invalid input to an integer

Example:

```python
print(10 / 0)
```

Output

```
ZeroDivisionError: division by zero
```

---

# Why Use Exception Handling?

Without exception handling, a program terminates immediately when an error occurs.

Exception handling allows us to:

- Prevent program crashes
- Display meaningful error messages
- Continue program execution
- Handle different errors gracefully

---

# try and except

The `try` block contains code that may raise an exception.

The `except` block handles the exception.

Syntax

```python
try:
    # Risky code
except ExceptionType:
    # Handle exception
```

Example

```python
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output

```
Cannot divide by zero.
```

---

# try, except and else

The `else` block executes **only if no exception occurs**.

Example

```python
try:
    num = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Division successful")
```

Output

```
Division successful
```

Flow

```
try
 │
 ├── Exception?
 │      │
 │      ├── Yes → except
 │      │
 │      └── No → else
```

---

# finally Block

The `finally` block always executes, whether an exception occurs or not.

Useful for:

- Closing files
- Closing database connections
- Releasing resources

Example

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Execution completed")
```

Output

```
Division by zero
Execution completed
```

---

# Complete Flow

```python
try:
    # Risky code
except:
    # Runs if exception occurs
else:
    # Runs if no exception occurs
finally:
    # Always runs
```

Execution order

```
try
 │
 ├── Exception?
 │      │
 │      ├── Yes → except → finally
 │      │
 │      └── No → else → finally
```

---

# Catching Multiple Exceptions

A program may raise different types of exceptions.

Example

```python
try:
    num = int(input("Enter number: "))
    print(100 / num)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Catching Multiple Exceptions Together

```python
try:
    value = int(input())
except (ValueError, TypeError):
    print("Invalid value")
```

---

# Generic Exception

Catch any exception using `Exception`.

```python
try:
    pass

except Exception as e:
    print(e)
```

`e` contains the actual error message.

Example

```
division by zero
```

---

# Raising Your Own Exception

Sometimes we intentionally stop execution when invalid data is provided.

Use the `raise` keyword.

Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output

```
ValueError: Age cannot be negative
```

---

# Custom Exception

You can create your own exception class by inheriting from `Exception`.

Example

```python
class InvalidAgeError(Exception):
    pass


age = -2

if age < 0:
    raise InvalidAgeError("Invalid age")
```

Output

```
InvalidAgeError: Invalid age
```

Example with handling

```python
class InvalidAgeError(Exception):
    pass

try:
    age = -10

    if age < 0:
        raise InvalidAgeError("Age must be positive")

except InvalidAgeError as e:
    print(e)
```

---

# File Handling

File handling allows Python programs to read from and write to files.

Common operations:

- Create file
- Read file
- Write file
- Append data
- Close file

---

# Opening a File

Syntax

```python
file = open("data.txt", "r")
```

Modes

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write (overwrites file) |
| a | Append |
| x | Create new file |
| rb | Read binary |
| wb | Write binary |

---

# Reading a File

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

---

# Reading Line by Line

```python
file = open("data.txt")

for line in file:
    print(line)

file.close()
```

---

# Writing to a File

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

`w` mode replaces existing content.

---

# Appending to a File

```python
file = open("data.txt", "a")

file.write("\nWelcome")

file.close()
```

`a` mode keeps existing content and adds new data.

---

# File Handling Using try-except

Example

```python
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist")

finally:
    file.close()
```

Problem:

If `open()` fails, `file` is never created, and `file.close()` raises another error.

Safer version

```python
file = None

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
```

---

# Using with Statement (Recommended)

Python automatically closes the file.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Advantages

- Automatically closes the file
- Cleaner code
- Prevents resource leaks
- Recommended in production code

---

# Difference Between open() and with

| open() | with open() |
|---------|-------------|
| Must manually close file | Automatically closes file |
| More chances of resource leaks | Safer |
| More code | Cleaner code |
| Error-prone | Recommended |

---

# Common File Exceptions

| Exception | Cause |
|-----------|-------|
| FileNotFoundError | File does not exist |
| PermissionError | No permission to access file |
| IsADirectoryError | Tried to open a directory as a file |
| UnicodeDecodeError | Wrong file encoding |

---

# Best Practices

- Use `with open()` whenever possible.
- Catch specific exceptions before generic ones.
- Avoid using a bare `except:`.
- Raise meaningful exceptions when validating input.
- Create custom exceptions for business-specific errors.
- Use `finally` only for cleanup tasks.

---

# Summary

| Topic | Purpose |
|--------|---------|
| try | Risky code |
| except | Handle exceptions |
| else | Executes if no exception occurs |
| finally | Always executes |
| raise | Raise an exception manually |
| Custom Exception | Create user-defined exceptions |
| open() | Open a file |
| read() | Read file contents |
| write() | Write data to a file |
| append() | Add data without removing existing content |
| with open() | Automatically closes the file |

---

# Key Takeaways

- Exceptions are runtime errors that interrupt program execution.
- `try-except` prevents unexpected program crashes.
- `else` runs only when no exception occurs.
- `finally` always executes, making it ideal for cleanup.
- Use `raise` to signal invalid conditions.
- Custom exceptions improve code readability and maintainability.
- Prefer `with open()` over `open()` for file handling.
- Always handle expected file-related exceptions gracefully.
