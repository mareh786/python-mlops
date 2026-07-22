"""
---------------------------------------------------------
Program: Check if Two Strings Differ by Exactly One Character

Approach:
- First, check if both strings have the same length.
- If the lengths differ, return a message indicating a mismatch.
- Traverse both strings character by character.
- Count the number of positions where the characters differ.
- After the traversal:
    - If the count is exactly 1, return True.
    - If the count is greater than 1, return False.
    - If the count is 0, the strings are identical.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each character is compared exactly once.)

Space Complexity:
- O(1)
  (Only a counter variable is used.)

Key Learning:
- Compare strings character by character.
- Count mismatches while traversing.
- This problem is commonly used to test string traversal logic.
---------------------------------------------------------
"""


def one_char_difference(str1, str2):
    # Check if the lengths are equal
    if len(str1) != len(str2):
        return "Word length mismatch"

    # Count differing characters
    different_char_count = 0

    # Compare characters one by one
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            different_char_count += 1

    # Return the result
    if different_char_count == 1:
        return True
    elif different_char_count > 1:
        return False
    else:
        return "Words are same"


# Driver Code
print(one_char_difference("adill", "adil"))
