
# Find the largest common prefix among three strings

def largest_common(str1, str2, str3):
    # Initialize an empty string to store the common prefix
    prefix = ""

    # Compare characters up to the length of the shortest string
    for i in range(min(len(str1), len(str2), len(str3))):
        # If the characters at the current index are the same in all strings
        if str1[i] == str2[i] == str3[i]:
            prefix += str1[i]
        else:
            # Stop when a mismatch is found
            break

    # Return the common prefix
    return prefix


# Example usage
val = largest_common("abc", "ahcd", "abd")
print(val)
