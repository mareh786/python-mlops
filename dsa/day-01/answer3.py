# -------------------- Sum of Digits of a Number --------------------

def sumofdig():

    # Take an integer input from the user
    a = int(input("Enter The Number: "))

    # Variable to store the sum of digits
    total = 0

    # Continue until all digits are processed
    while a > 0:

        # Extract the last digit using the modulo operator
        digit = a % 10

        # Add the extracted digit to the running total
        total += digit

        # Remove the last digit using floor division
        a //= 10

    # Return the final sum of digits
    return total


# Call the function and print the result
print(sumofdig())