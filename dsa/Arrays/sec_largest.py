"""
---------------------------------------------------------
Program: Find the Second Largest Element in an Array

Approach:
- Check if the array contains at least two elements.
- Initialize `largest` and `second_largest` with negative infinity.
- Traverse the array once.
- If the current element is greater than `largest`:
    - Update `second_largest` with the current `largest`.
    - Update `largest` with the current element.
- Otherwise, if the current element is greater than
  `second_largest` and not equal to `largest`,
  update `second_largest`.
- Return the second largest element.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed only once.)

Space Complexity:
- O(1)
  (Only two extra variables are used.)

Key Learning:
- The largest and second largest elements can be found in a
  single traversal.
- Avoid sorting the array, which would increase the time
  complexity to O(n log n).
- The condition `num != largest` prevents duplicate largest
  values from being considered as the second largest.
---------------------------------------------------------
"""

from numpy import array


def second_largest(arr):
    # Array should contain at least two elements
    if len(arr) < 2:
        return "Array must contain at least 2 elements"

    # Initialize largest and second largest
    largest = float('-inf')
    second_largest = float('-inf')

    # Traverse the array
    for num in arr:

        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num

        # Update second largest if applicable
        elif num > second_largest and num != largest:
            second_largest = num

    # Check if second largest exists
    if second_largest == float('-inf'):
        return "Second largest element does not exist."

    return second_largest


# Driver Code
arr = array([9, 7, 8, 5, 12])

print("Second Largest Element:", second_largest(arr))
