# Finding the maximum in the numbers

def check_maximum():
    num1 = 199
    num2 = 1399
    num3 = 19
    if num1 > num2 and num1 > num3:
        print("The maximum number is:", num1)
    elif num2 > num1 and num2 > num3:
        print("The maximum number is:", num2)
    else:
        print("The maximum number is:", num3)
        
check_maximum()

