
"""
---------------------------------------------------------
Program: Longest Substring Without Repeating Characters

Approach:
- Use the Sliding Window technique with two pointers.
- Maintain a set to store the unique characters in the current
  window.
- Expand the window by moving the right pointer.
- If a duplicate character is encountered:
    - Shrink the window from the left until the duplicate is removed.
- Update the maximum length of the window after each expansion.
- Return the maximum length.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each character is added to and removed from the set at most once.)

Space Complexity:
- O(n)
  (The set stores at most all unique characters in the string.)

Key Learning:
- The Sliding Window technique is ideal for problems involving
  contiguous substrings.
- A set provides O(1) average-time membership checking.
- This is one of the most frequently asked string interview
  questions.
---------------------------------------------------------
"""


def unique_substring(text):
    # Left pointer of the sliding window
    left = 0

    # Store unique characters in the current window
    seen = set()

    # Store the maximum length found
    max_len = 0

    # Expand the window using the right pointer
    for right in range(len(text)):

        # Remove characters until the duplicate is removed
        while text[right] in seen:
            seen.remove(text[left])
            left += 1

        # Add the current character
        seen.add(text[right])

        # Update the maximum window length
        max_len = max(max_len, right - left + 1)

    return max_len


# Driver Code
print("Longest Unique Substring Length:", unique_substring("abcbcbc"))
