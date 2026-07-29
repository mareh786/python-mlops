"""
---------------------------------------------------------
Program: Check if Two Strings are Mirror Images

Approach:
- Two strings are mirror images if one string is the reverse
  of the other.
- First, check if both strings have the same length.
- Use two pointers:
    - One starts from the beginning of the first string.
    - The other starts from the end of the second string.
- Compare characters at both pointers.
- If any pair of characters does not match, the strings are
  not mirror images.
- If all characters match, the strings are mirror images.

Time Complexity:
- Best Case: O(1)
  (Mismatch occurs at the first character.)

- Average Case: O(n)

- Worst Case: O(n)
  (All characters are compared.)

Space Complexity:
- O(1)
  (Only two pointer variables are used.)

Key Learning:
- Two-pointer traversal is an efficient technique for
  comparing a string with the reverse of another string.
- This avoids creating a new reversed string.
---------------------------------------------------------
"""


def is_mirror_image(str1, str2):
    # Check if the lengths are equal
    if len(str1) != len(str2):
        return "Strings are not mirror images"

    # Initialize pointers
    i = 0
    j = len(str2) - 1

    # Compare characters
    while i < len(str1):
        if str1[i] != str2[j]:
            return "Strings are not mirror images"

        i += 1
        j -= 1

    return "Strings are mirror images"


# Driver Code
print(is_mirror_image("abc", "cba"))
