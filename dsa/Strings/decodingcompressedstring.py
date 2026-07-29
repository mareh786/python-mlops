"""
---------------------------------------------------------
Program: Decode a Compressed String

Example:
Input : "a2b3c4"
Output: "aabbbcccc"

Approach:
- Initialize an empty string to store the decoded result.
- Traverse the string from index 1.
- Whenever a digit is encountered:
    - Repeat the previous character by the given number of times.
    - Append it to the result.
- Return the decoded string.

Assumption:
- Every character is immediately followed by a single-digit count.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n + k)

  where:
  - n = length of the compressed string
  - k = length of the decoded string

Space Complexity:
- O(k)
  (The decoded string is stored in memory.)

Key Learning:
- Strings can be expanded using the multiplication operator.
- `'a' * 3` produces `"aaa"`.
- This problem is a common string traversal interview question.
---------------------------------------------------------
"""


def decode_compressed_string(text):
    # Store the decoded string
    decoded = ""

    # Traverse the string
    for i in range(1, len(text)):

        # Check if the current character is a digit
        if text[i].isdigit():

            # Repeat the previous character
            decoded += text[i - 1] * int(text[i])

    return decoded


# Driver Code
print("Decoded String:", decode_compressed_string("a2b3c4"))
