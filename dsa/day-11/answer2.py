# Capitalize the First Letter of Each Word

def capitalize_word(text):
    # Split the sentence into individual words
    words = text.split()

    # Capitalize the first letter of each word and join them back
    result = " ".join([word.capitalize() for word in words])

    # Return the formatted string
    return result


# Call the function and print the result
d = capitalize_word("python is beautiful")
print(d)
