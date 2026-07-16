"""
---------------------------------------------------------
Program: Remove Duplicate Elements from an Array

Approach:
- Convert the array into a set.
- A set automatically removes all duplicate elements.
- Convert the set back into a list.
- Return the list containing unique elements.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Every element is processed while creating the set.)

Space Complexity:
- O(n)
  (An additional set is created to store unique elements.)

Key Learning:
- A Python set stores only unique values.
- This is the simplest approach to remove duplicates.
- The order of elements is NOT preserved because sets are unordered.
- If the order must be preserved, use a different approach.
---------------------------------------------------------
"""

from numpy import array


def remove_duplicates(arr):
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)

    # Convert the set back to a list
    result = list(unique_elements)

    return result


# Driver Code
arr = array([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4])

print("Array after removing duplicates:", remove_duplicates(arr))
