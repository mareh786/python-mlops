
"""
---------------------------------------------------------
Program: Check if One String is a Subsequence of Another

Approach:
- Use two pointers:
    - `i` for the first string (subsequence).
    - `j` for the second string.
- Traverse the second string.
- If the characters at both pointers match, move `i` forward.
- Always move `j` forward.
- After traversal, if `i` reaches the end of the first string,
  then the first string is a subsequence of the second string.

Time Complexity:
- Best Case: O(1)
  (If the first string is empty.)

- Average Case: O(n)

- Worst Case: O(n)
  (Each character of the second string is visited once.)

  where n = length of the second string.

Space Complexity:
- O(1)
  (Only two pointer variables are used.)

Key Learning:
- The Two Pointer Technique is ideal for subsequence problems.
- A subsequence preserves the order of characters but not
  necessarily their contiguity.
---------------------------------------------------------
"""


def is_subsequence(s1, s2):
    # Pointer for the first string
    i = 0

    # Pointer for the second string
    j = 0

    # Traverse both strings
    while i < len(s1) and j < len(s2):

        # Characters match
        if s1[i] == s2[j]:
            i += 1

        # Always move the second pointer
        j += 1

    # If all characters of s1 were matched
    return i == len(s1)


# Driver Code
print("Is Subsequence:", is_subsequence("abc", "avbcd"))
