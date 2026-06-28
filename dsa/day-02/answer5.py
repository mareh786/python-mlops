# -------------------- Removing Spaces from a String --------------------

def removeSpaces():

    # Original string containing multiple spaces
    text = "A d           I L            "

    # Variable to store the string without spaces
    newstr = ""

    # Iterate through each character in the string
    for each in text:

        # Skip the character if it is a space
        if each == ' ':
            continue

        # Otherwise, add the character to the new string
        else:
            newstr += each

    # Return the string after removing all spaces
    return newstr


# Call the function and store the returned value
finalstr = removeSpaces()

# Display the result
print(f"The final string is {finalstr}")