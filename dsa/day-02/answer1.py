# -------------------- Checking Whether a String is a Palindrome --------------------

def isPalindrome():

    # Take a string input from the user
    text = input("Enter the string: ")

    # Convert the string to lowercase for case-insensitive comparison
    text = text.lower()

    # Check if the string is equal to its reverse
    if text == text[::-1]:

        # Display a success message if it is a palindrome
        print(f"The given string '{text}' is a Palindrome")

    else:

        # Display a message if it is not a palindrome
        print(f"The given string '{text}' is not a Palindrome")


# Call the function
isPalindrome()