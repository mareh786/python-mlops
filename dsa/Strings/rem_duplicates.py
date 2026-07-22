
"""
---------------------------------------------------------
Program: Remove Consecutive Duplicate Characters

Approach:
- If the string is empty, return it.
- Initialize the result string with the first character.
- Traverse the string from the second character onward.
- Compare the current character with the previous character.
- If they are different, append the current character to the result.
- Return the final string.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each character is processed exactly once.)

Space Complexity:
- O(n)
  (A new string is created to store the result.)

Key Learning:
- Compare each character with its previous character.
- Only consecutive duplicates are removed.
- Non-consecutive duplicate characters remain unchanged.
---------------------------------------------------------
"""


def remove_consecutive_duplicates(text):
    # Handle empty string
    if len(text) == 0:
        return ""

    # Initialize result with the first character
    result = text[0]

    # Traverse from the second character
    for i in range(1, len(text)):

        # Append only if current character is different
        if text[i] != text[i - 1]:
            result += text[i]

    return result


# Driver Code
print("Result:", remove_consecutive_duplicates("aaabbbbccddddaa"))
