# Write a function that prints the right angled triangle pattern

def design(num):
    for i in range(1, num+1):
        print("* "* i)
design(7)

def invDesign(rows):
    for i in range(rows, 0, -1):
        print("* "*i)

invDesign(7)