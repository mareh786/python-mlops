n1 = int(input("Enter a Number: "))

#print(f"The user entered: {number}")

if n1 < 10:
    print(f"The number user entered is {n1}, which is single digit number")
else:
    print(f"The number user entered is {n1}, which is not single digit number")

n2 = int(input("Enter another number: "))

#Now lets compare the number

if n1 == n2:
    print(f"The numbers are same so the product of them is n^2: {n1*n2}")
else: 
    print(f"The numbers are different hence it's product is n1*n2: {n1*n2}")

if n2 < 100:
    if n2 > 9:
        print(f"The provided number is a two digit number")
    else: 
        print(f"The number is single digit number")
else: 
    print("The number is 3 digit number")

n3 = int(input("Enter the third number: "))

if n1 > n2 and n1 > n3:
    print(f"The first number is the largest")
elif n2 > n1 and n2 > n3:
    print(f"The second number is the largest")
elif n3 > n1 and n3 > n1:
    print(f"The third number is the largest")