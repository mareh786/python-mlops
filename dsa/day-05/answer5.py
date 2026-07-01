# Problem 5: Print an Inverted Star Pattern

def invDesign(rows):
    for i in range(rows, 0, -1):
        print("*"*i)

invDesign(7)