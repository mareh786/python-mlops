#[expression for item in iterable if condition]

a = [
    "A",
    "B1",
    "C",
    "D1"
    ]

ones = [ y for y in a if "1" in y]

print(ones)

nums = ["1", "2", "3", "4", "5", "6"]

even = [x for x in nums if int(x)%2==0 ]

print(even)

names = ["adil", "rehan", "mohammed"]

caps= [x.upper() for x in names]

print(caps)

num = ['1', '2', '3', '4', '5']

sqr = [int(x)**2 for x in num if int(x)**2 > 1]

print(sqr)

words = ["apple", "bat", "car", "elephant"]

longerword = [x for x in words if len(x)> 3]

print(longerword)

number = [10, 15, 20, 25, 30]

div = [x for x in number if x%5==0 and x%10==0]

print(div)

word = ["apple", "banana", "cherry", "date"]

a = [(x, len(x)) for x in word]

print(a)

work = ["cleaning", "eating", "sleeping", "Cheat"]

noIng = [x for x in work if "ing" not in x]

print(noIng)