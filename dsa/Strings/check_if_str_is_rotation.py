"""
---------------------------------------------------------
Program: Check if One String is a Rotation of Another

Approach:
- If the lengths of both strings are different, they cannot
  be rotations of each other.
- Concatenate the first string with itself.
- If the second string is a substring of the concatenated
  string, then it is a rotation of the first string.
- Otherwise, it is not a rotation.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n²)
  (Substring search is efficient in Python, but the theoretical
  worst case can be quadratic depending on the implementation.)

Space Complexity:
- O(n)
  (A new string of length 2n is created.)

Key Learning:
- A rotation of a string always appears as a substring of the
  original string concatenated with itself.
- This is one of the most common interview tricks for rotation
  problems.
---------------------------------------------------------
"""


def is_rotation(str1, str2):
    # Strings with different lengths cannot be rotations
    if len(str1) != len(str2):
        return f'"{str2}" is not a rotation of "{str1}"'

    # Concatenate the first string with itself
    doubled_string = str1 + str1

    # Check if the second string is a substring
    if str2 in doubled_string:
        return f'"{str2}" is a rotation of "{str1}"'
    else:
        return f'"{str2}" is not a rotation of "{str1}"'


# Driver Code
print(is_rotation("adil", "ladi"))
