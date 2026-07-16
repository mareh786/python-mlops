"""
---------------------------------------------------------
Program: Find the Sum of Maximum and Minimum Elements in an Array

Approach:
- Assume the first element is both the minimum and maximum.
- Traverse the array once.
- Update the maximum if a larger element is found.
- Update the minimum if a smaller element is found.
- Return both minimum and maximum values.
- Add the minimum and maximum values and return their sum.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Every element is visited exactly once.)

Space Complexity:
- O(1)
  (Only two extra variables are used to store the minimum and maximum.)

Key Learning:
- Both minimum and maximum can be found in a single traversal.
- Performing multiple operations in one pass improves efficiency.
- Avoid naming functions with built-in names like `sum()`.
---------------------------------------------------------
"""

from numpy import array


def find_min_max(arr):
    # Assume the first element is both minimum and maximum
    min_val = arr[0]
    max_val = arr[0]

    # Traverse the array
    for num in arr:

        # Update maximum value
        if num > max_val:
            max_val = num

        # Update minimum value
        if num < min_val:
            min_val = num

    # Return both values
    return min_val, max_val


def sum_of_min_max(arr):
    # Get the minimum and maximum values
    min_val, max_val = find_min_max(arr)

    # Return their sum
    return min_val + max_val


# Driver Code
arr = array([4, 6, 8, 2, 98])

print("Sum of Minimum and Maximum:", sum_of_min_max(arr))
