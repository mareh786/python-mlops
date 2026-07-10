# Count uppercase, lowercase, and special characters in a string

def count_case(text):
    # Initialize counters
    upper_count = 0
    lower_count = 0
    special_chars = []

    # Traverse each character in the string
    for ch in text:
        # Check if the character is uppercase
        if ch.isupper():
            upper_count += 1

        # Check if the character is lowercase
        elif ch.islower():
            lower_count += 1

        # Store special characters, digits, and spaces
        else:
            special_chars.append(ch)

    # Return the counts and list of special characters
    return upper_count, lower_count, special_chars


# Call the function and print the result
print(count_case("Adil@1"))
