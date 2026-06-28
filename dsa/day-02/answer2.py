# -------------------- Finding the Maximum Number in a List --------------------

def maxNum():

    # Create a list of numbers stored as strings
    list1 = ['111', '192', '333', '414']

    # Assume the first element is the maximum initially
    maxnum = int(list1[0])

    # Iterate through each element in the list
    for num in list1:

        # Convert the current string value to an integer
        current_num = int(num)

        # Update maxnum if a larger value is found
        if current_num > maxnum:
            maxnum = current_num

    # Return the maximum number
    return maxnum


# Call the function and print the result
print(maxNum())