"""
---------------------------------------------------------
Program: Move All Zeros to the End of an Array

Approach:
- Create two separate lists:
    - `non_zeros` to store all non-zero elements.
    - `zeros` to store all zero elements.
- Traverse the array once.
- Append each element to the appropriate list.
- Concatenate the `non_zeros` list with the `zeros` list.
- Return the resulting array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed only once.)

Space Complexity:
- O(n)
  (Two additional lists are used to store the elements.)

Key Learning:
- Array partitioning based on a condition.
- Preserves the relative order of non-zero elements.
- This is a simple approach but uses extra space.
- An optimized in-place solution exists with O(1) extra space.
---------------------------------------------------------
"""

from numpy import array


def move_zeros_to_end(arr):
    # List to store non-zero elements
    non_zeros = []

    # List to store zero elements
    zeros = []

    # Traverse the array
    for num in arr:

        # Store non-zero elements
        if num != 0:
            non_zeros.append(num)

        # Store zero elements
        else:
            zeros.append(num)

    # Concatenate non-zero and zero lists
    result = non_zeros + zeros

    return result


# Driver Code
arr = array([0, 1, 4, 0, 5])

print("Array after moving zeros:", move_zeros_to_end(arr))
