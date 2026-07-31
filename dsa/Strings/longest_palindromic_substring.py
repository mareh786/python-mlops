"""
---------------------------------------------------------
Program: Find the Longest Palindromic Substring

Approach:
- Treat every character as the center of a palindrome.
- Expand outward to check for:
    1. Odd-length palindromes (single center).
    2. Even-length palindromes (two centers).
- Whenever a longer palindrome is found:
    - Update the result string.
    - Update the maximum length.
- Return the longest palindromic substring and its length.

Time Complexity:
- Best Case: O(n)
  (Very few expansions.)

- Average Case: O(n²)

- Worst Case: O(n²)
  (Every center expands across most of the string.)

Space Complexity:
- O(1)
  (Only a few variables are used, excluding the output string.)

Key Learning:
- Expanding around every possible center finds all palindromes.
- Every palindrome has either:
    - One center (odd length), or
    - Two centers (even length).
- This is the standard interview solution.
---------------------------------------------------------
"""


def longest_palindromic(text):
    # Store the longest palindrome
    result = ""

    # Store its length
    result_len = 0

    # Consider each character as the center
    for i in range(len(text)):

        # -------------------------
        # Odd Length Palindrome
        # -------------------------
        left = i
        right = i

        while left >= 0 and right < len(text) and text[left] == text[right]:

            if (right - left + 1) > result_len:
                result = text[left:right + 1]
                result_len = right - left + 1

            left -= 1
            right += 1

        # -------------------------
        # Even Length Palindrome
        # -------------------------
        left = i
        right = i + 1

        while left >= 0 and right < len(text) and text[left] == text[right]:

            if (right - left + 1) > result_len:
                result = text[left:right + 1]
                result_len = right - left + 1

            left -= 1
            right += 1

    return result, result_len


# Driver Code
print(longest_palindromic("ababad"))
