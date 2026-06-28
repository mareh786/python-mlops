# -------------------- Finding the Maximum Number (Reusable Version) --------------------

def check_maximum(num1, num2, num3):

    # Compare all three numbers
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


# Store the returned value in a variable
maximum_number = check_maximum(199, 1399, 19)

# Print the result
print("The maximum number is:", maximum_number)