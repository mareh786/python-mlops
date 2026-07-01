# Problem 3: Check if Two Strings are Equal (Ignoring Case)


def sameStr():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    if str1.lower().strip().replace(" ", "")==str2.lower().strip().replace(" ", ""):
        print(f"The given strings are same")
    else:
        print(f"The given strings are not same")
sameStr()