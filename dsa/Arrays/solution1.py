"""
---------------------------------------------------------
Program: Find the Maximum Element in an Array

Approach:
- Traverse the array from left to right.
- Keep track of the maximum element found so far.
- Update the maximum whenever a larger element is encountered.
- Return the maximum element after traversing the entire array.

Time Complexity:
- O(n), where n is the number of elements in the array.
  (Each element is visited exactly once.)

Space Complexity:
- O(1)
  (Only one extra variable is used to store the maximum value.)
---------------------------------------------------------
"""

from numpy import array


def maximum_element():
    # Create a NumPy array
    values = array([10, 25, 7, 89, 45])

    # Initialize maximum with negative infinity
    maximum = float('-inf')

    # Traverse the array
    for num in values:
        # Update maximum if a larger element is found
        if num > maximum:
            maximum = num

    # Return the maximum element
    return maximum


# Driver code
print("Maximum element:", maximum_element())
