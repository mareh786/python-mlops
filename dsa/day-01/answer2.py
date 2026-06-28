




def vowelCounter():

    a = input("Enter the string: ").lower()
    c = 0

    for each in a:
        if each in ["a", "e", "i", "o", "u"]:
            c += 1
    return c

count=vowelCounter()
    
print(count)