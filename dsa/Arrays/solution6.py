"""
---------------------------------------------------------
Program: Find the Smallest Element in an Array

Approach:
- Assume the first element is the smallest.
- Traverse the array from left to right.
- Compare each element with the current smallest value.
- Update the smallest value whenever a smaller element is found.
- Return the smallest element after traversing the entire array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Every element must be checked to ensure it is the smallest.)

Space Complexity:
- O(1)
  (Only one extra variable is used to store the smallest element.)

Key Learning:
- Maintaining a running minimum while traversing an array.
- Single-pass traversal is sufficient to find the minimum.
- Efficient approach without sorting the array.
---------------------------------------------------------
"""

from numpy import array


def smallest_element(arr):
    # Assume the first element is the smallest
    smallest = arr[0]

    # Traverse the array
    for num in arr:

        # Update the smallest element if a smaller value is found
        if num < smallest:
            smallest = num

    # Return the smallest element
    return smallest


# Driver Code
arr = array([12, 5, 8, 9])

print("Smallest element:", smallest_element(arr))
