# Find the missing character(s) from str2 that are not present in str1

def missing_char(str1, str2):
    # Create a list to store missing characters
    missing = []

    # Check each character in str2
    for ch in str2:
        # If the character is not found in str1, add it to the list
        if ch not in str1:
            missing.append(ch)

    # Return the list of missing characters
    return missing


# Test the function
v1 = missing_char("abcd", "decba")

# Display the result
if len(v1) == 0:
    print("No chars missing")
else:
    print(f"The missing chars are {v1}")
