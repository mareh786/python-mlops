"""
---------------------------------------------------------
Program: Find the Second Smallest Element in an Array

Approach:
- Check if the array contains at least two elements.
- Initialize `smallest` and `second_smallest` with positive infinity.
- Traverse the array once.
- If the current element is smaller than `smallest`:
    - Update `second_smallest` with the current `smallest`.
    - Update `smallest` with the current element.
- Otherwise, if the current element is smaller than
  `second_smallest` and not equal to `smallest`,
  update `second_smallest`.
- Return the second smallest element.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed only once.)

Space Complexity:
- O(1)
  (Only two extra variables are used.)

Key Learning:
- The smallest and second smallest elements can be found in a
  single traversal.
- Avoid sorting the array, which would increase the time
  complexity to O(n log n).
- The condition `num != smallest` ensures duplicate smallest
  values are not considered as the second smallest.
---------------------------------------------------------
"""

from numpy import array


def second_smallest(arr):
    # Array should contain at least two elements
    if len(arr) < 2:
        return "Array must contain at least 2 elements."

    # Initialize smallest and second smallest
    smallest = float('inf')
    second_smallest = float('inf')

    # Traverse the array
    for num in arr:

        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

        # Update second smallest if applicable
        elif num < second_smallest and num != smallest:
            second_smallest = num

    # Check if second smallest exists
    if second_smallest == float('inf'):
        return "Second smallest element does not exist."

    return second_smallest


# Driver Code
arr = array([12, 5, 8, 9])

print("Second Smallest Element:", second_smallest(arr))
