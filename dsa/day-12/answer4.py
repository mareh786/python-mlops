# Check if one string is a rotation of another string

def check_rotation(str1, str2):
    # Concatenate the first string with itself
    doubled = str1 + str1

    # If the lengths are different, they cannot be rotations
    if len(str1) != len(str2):
        return False

    # Check if the second string exists in the doubled string
    elif str2 in doubled:
        return True

    # Otherwise, they are not rotations
    else:
        return False


# Call the function and print the result
print(check_rotation("abcd", "dbac"))
