"""
---------------------------------------------------------
Program: Find the Last Occurrence of an Element in an Array

Approach:
- Initialize a variable `last_index` with -1.
- Traverse the array from left to right.
- Whenever the target element is found, update `last_index`.
- Continue traversing until the end of the array.
- Return `last_index`.
- If the target is not found, `last_index` remains -1.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The entire array must be traversed to find the last occurrence.)

Space Complexity:
- O(1)
  (Only one extra variable is used.)

Key Learning:
- Unlike finding the first occurrence, we cannot stop after finding
  the target because there may be another occurrence later.
- Keeping track of the latest matching index gives the last occurrence.
---------------------------------------------------------
"""

from numpy import array


def find_last_occurrence(arr, target):
    # Initialize last_index to -1 (target not found)
    last_index = -1

    # Traverse the array
    for i in range(len(arr)):

        # Update last_index whenever the target is found
        if arr[i] == target:
            last_index = i

    # Return the last occurrence index
    return last_index


# Driver Code
arr = array([1, 2, 3, 2, 3, 4, 3])

print("Last occurrence index:", find_last_occurrence(arr, 9))
