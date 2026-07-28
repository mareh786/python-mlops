"""
---------------------------------------------------------
Program: Find the Longest Palindromic Prefix

Approach:
- Start by considering the entire string as a prefix.
- Traverse from the full length of the string down to 1.
- Extract the prefix of length `i`.
- Check whether the prefix is equal to its reverse.
- Return the first palindromic prefix found.
- If no palindrome exists (except the empty string), return "".

Time Complexity:
- Best Case: O(n)
  (The entire string is already a palindrome.)

- Average Case: O(n²)

- Worst Case: O(n²)
  (For each prefix, a palindrome check takes O(n).)

Space Complexity:
- O(n)
  (A new substring and its reverse are created.)

Key Learning:
- A palindrome reads the same forwards and backwards.
- Since we're checking prefixes from longest to shortest,
  the first palindrome found is the longest palindromic prefix.
---------------------------------------------------------
"""


def longest_prefix_palindrome(text):
    # Check prefixes from longest to shortest
    for i in range(len(text), 0, -1):

        # Extract the current prefix
        prefix = text[:i]

        # Check if the prefix is a palindrome
        if prefix == prefix[::-1]:
            return prefix

    return ""


# Driver Code
print("Longest Palindromic Prefix:", longest_prefix_palindrome("levelup"))
