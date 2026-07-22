
"""
---------------------------------------------------------
Program: Find the Longest Common Prefix of Three Strings

Approach:
- Find the length of the shortest string.
- Traverse all three strings character by character.
- Compare the characters at the same index.
- If all characters match, add the character to the prefix.
- Stop as soon as a mismatch is found.
- Return the accumulated prefix.

Time Complexity:
- Best Case: O(1)
  (Mismatch occurs at the first character.)

- Average Case: O(n)

- Worst Case: O(n)
  (All characters of the shortest string are compared.)

  where n = length of the shortest string.

Space Complexity:
- O(n)
  (A new string is created to store the common prefix.)

Key Learning:
- Compare strings character by character until a mismatch occurs.
- The longest possible prefix is limited by the shortest string.
- This is a common interview problem on strings.
---------------------------------------------------------
"""


def common_prefix(str1, str2, str3):
    # Store the common prefix
    prefix = ""

    # Traverse up to the length of the shortest string
    for i in range(min(len(str1), len(str2), len(str3))):

        # Check if all three characters are equal
        if str1[i] == str2[i] == str3[i]:
            prefix += str1[i]

        # Stop when a mismatch occurs
        else:
            break

    return prefix


# Driver Code
print("Longest Common Prefix:", common_prefix("adil", "adila", "adilad"))
