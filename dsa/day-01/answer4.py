# -------------------- Approach 1: Using Slicing --------------------

# Define a string
string = "adil"

# Reverse the string using slicing [start:stop:step]
# step = -1 means move backwards
print(string[::-1])


# -------------------- Approach 2: Using Loop --------------------

def revStr():

    # Take string input from the user
    str_input = input("Enter the string: ")

    # Variable to store reversed string
    result = ""

    # Loop from last index to first index
    for i in range(len(str_input) - 1, -1, -1):

        # Append each character in reverse order
        result += str_input[i]

    # Return reversed string
    return result


# Call the function and print result
print(revStr())