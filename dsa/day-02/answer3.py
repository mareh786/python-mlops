# -------------------- Counting Consonants in a Word --------------------

def consonant():

    # Define the input string
    text = "Mohammed"

    # Convert the string to lowercase for uniform comparison
    text = text.lower()

    # Initialize a counter for consonants
    count = 0

    # Iterate through each character in the string
    for ch in text:

        # Check if the character is NOT a vowel
        if ch not in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    # Return the total number of consonants
    return count


# Store the returned value
consonants = consonant()

# Display the result
print(f"The number of consonants in the word is {consonants}")