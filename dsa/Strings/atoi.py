"""
---------------------------------------------------------
Program: String to Integer (atoi)

Approach:
- Remove leading and trailing spaces using `strip()`.
- If the string is empty, return 0.
- Check for an optional '+' or '-' sign.
- Traverse the remaining characters:
    - Stop when a non-digit character is encountered.
    - Convert each digit into an integer.
- Apply the sign to the result.
- Clamp the result to the 32-bit signed integer range.
- Return the final integer.

Time Complexity:
- Best Case: O(1)
  (Empty string or first character is invalid.)

- Average Case: O(n)

- Worst Case: O(n)
  (Every character is processed once.)

Space Complexity:
- O(1)
  (Only a few variables are used.)

Key Learning:
- Process the string character by character.
- Handle optional signs (+/-) separately.
- Stop parsing at the first non-digit character.
- Clamp the answer to the 32-bit signed integer range.
---------------------------------------------------------
"""


def my_atoi(text):
    # Remove leading and trailing spaces
    s = text.strip()

    # Return 0 if the string is empty
    if not s:
        return 0

    # Default sign is positive
    sign = 1

    # Store the resulting integer
    result = 0

    # Check for optional sign
    if s[0] == "-" or s[0] == "+":
        if s[0] == "-":
            sign = -1

        # Remove the sign character
        s = s[1:]

    # Convert digits to an integer
    for ch in s:
        if not ch.isdigit():
            break

        result = result * 10 + int(ch)

    # Apply the sign
    result *= sign

    # Clamp to 32-bit signed integer range
    if result > 2**31 - 1:
        return 2**31 - 1

    elif result < -2**31:
        return -2**31

    return result


# Driver Code
print("Converted Integer:", my_atoi(" -123abc"))
