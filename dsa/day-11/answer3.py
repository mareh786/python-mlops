
# Find the Common Letters in Two Strings

# Approach 1: Using nested loops and a set
def common(str1, str2):
    # Create a set to store unique common letters
    common_letters = set()

    # Compare each character of the first string with the second string
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i].lower() == str2[j].lower():
                common_letters.add(str1[i].lower())

    # Return the set of common letters
    return common_letters


# Example
# print(common("Apple", "graPe"))


# Approach 2: Using membership checking
def common_letter(str1, str2):
    # Create an empty list to store common letters
    result = []

    # Traverse each character of the first string
    for ch in str1.lower():
        # Add the character only if it is unique and present in the second string
        if ch not in result and ch in str2.lower():
            result.append(ch)

    # Return the list of common letters
    return result


# Call the function and print the result
print(common_letter("Apple", "graPe"))
