# -------------------- Sum of Even Numbers in a List --------------------

def addition():

    # List of numbers stored as strings
    list1 = ['1', '12', '3', '14']

    # Variable to store the sum of even numbers
    total = 0

    # Iterate through each element in the list
    for each in list1:

        # Convert the current string to an integer
        number = int(each)

        # Check if the number is even
        if number % 2 == 0:

            # Add the even number to the running total
            total += number

    # Return the final sum
    return total


# Call the function and store the returned value
sum_of_even_numbers = addition()

# Display the result
print(f"The sum of even numbers in the list is {sum_of_even_numbers}")