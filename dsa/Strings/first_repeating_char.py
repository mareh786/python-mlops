"""
---------------------------------------------------------
Program: Find the First Repeating Character in a String

Approach:
- Initialize an empty string (or set) to keep track of the
  characters seen so far.
- Traverse the string from left to right.
- If the current character has already been seen, return it
  as the first repeating character.
- Otherwise, add the character to the seen collection.
- If no repeating character exists, return an appropriate
  message.

Time Complexity:
- Best Case: O(1)
  (The first repeated character is found immediately.)

- Average Case: O(n²)
- Worst Case: O(n²)
  (`ch in temp` performs a linear search on the string.)

Space Complexity:
- O(n)
  (The seen characters are stored.)

Key Learning:
- Keep track of previously seen characters while traversing.
- Using a string for membership checking is simple but not
  optimal.
- Using a `set` reduces the time complexity to O(n).
---------------------------------------------------------
"""


def first_repeat_letter(text):
    # String to store seen characters
    seen = ""

    # Traverse the string
    for ch in text:

        # Check if the character has already appeared
        if ch in seen:
            return ch

        # Otherwise, store it
        else:
            seen += ch

    # No repeating character found
    return "No repeating character found"


# Driver Code
print("First Repeating Character:", first_repeat_letter("abcad"))
