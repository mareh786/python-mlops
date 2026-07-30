"""
---------------------------------------------------------
Program: Find the Maximum Consecutive Occurrence of a Character

Approach:
- Initialize two counters:
    - count: Stores the current consecutive occurrences.
    - max_count: Stores the maximum consecutive occurrences.
- Traverse the string character by character.
- If the current character matches the target character:
    - Increment count.
    - Update max_count if needed.
- Otherwise:
    - Reset count to 0.
- Return max_count after traversing the string.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each character is visited exactly once.)

Space Complexity:
- O(1)
  (Only a few integer variables are used.)

Key Learning:
- Running counters are useful for tracking consecutive
  occurrences.
- Reset the counter whenever a different character is found.
- This pattern is commonly used in string and array problems.
---------------------------------------------------------
"""


def max_consecutive_char(text, target):
    # Current consecutive count
    count = 0

    # Maximum consecutive count
    max_count = 0

    # Traverse the string
    for ch in text:

        # If the current character matches the target
        if ch == target:
            count += 1

            # Update the maximum count
            max_count = max(max_count, count)

        # Reset the count if a different character is found
        else:
            count = 0

    return max_count


# Driver Code
print("Maximum Consecutive Occurrence:",
      max_consecutive_char("aabbbcbbcccccc", "c"))
