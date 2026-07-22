"""
---------------------------------------------------------
Program: Toggle the Case of Characters in a String

Approach:
- Initialize an empty string `result`.
- Traverse each character in the string.
- If the character is uppercase, convert it to lowercase.
- If the character is lowercase, convert it to uppercase.
- Leave digits and special characters unchanged.
- Return the resulting string.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each character is processed exactly once.)

Space Complexity:
- O(n)
  (A new string is created to store the toggled characters.)

Key Learning:
- `isupper()` checks whether a character is uppercase.
- `islower()` checks whether a character is lowercase.
- `upper()` and `lower()` perform case conversion.
- Strings are immutable in Python, so a new string is created.
---------------------------------------------------------
"""


def toggle_case(text):
    # Initialize an empty string
    result = ""

    # Traverse each character
    for ch in text:

        # Convert uppercase to lowercase
        if ch.isupper():
            result += ch.lower()

        # Convert lowercase to uppercase
        elif ch.islower():
            result += ch.upper()

        # Leave digits and special characters unchanged
        else:
            result += ch

    return result


# Driver Code
print("Toggled String:", toggle_case("Adil@12A"))
