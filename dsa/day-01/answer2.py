# -------------------- Counting Vowels in a String --------------------

def vowelCounter():

    # Take a string input from the user and convert it to lowercase
    # so that both uppercase and lowercase vowels are handled uniformly
    a = input("Enter the string: ").lower()

    # Initialize a counter for vowels
    c = 0

    # Iterate through each character in the string
    for each in a:

        # Check if the character is a vowel
        if each in ["a", "e", "i", "o", "u"]:
            c += 1

    # Return the total number of vowels
    return c


# Call the function and store the returned value
count = vowelCounter()

# Display the result
print("Number of vowels:", count)