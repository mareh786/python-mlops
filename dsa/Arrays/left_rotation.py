"""
---------------------------------------------------------
Program: Left Rotation of an Array

Approach 1: Rotate Left by One Position (Reversal Algorithm)
- Reverse the first element (no change).
- Reverse the remaining (n-1) elements.
- Reverse the entire array.
- The first element moves to the last position.

Approach 2: Rotate Left by k Positions (Reversal Algorithm)
- Compute n = n % len(arr) to handle large rotations.
- Reverse the first n elements.
- Reverse the remaining elements.
- Reverse the entire array.
- The array gets rotated left by n positions.

Time Complexity:
- Rotate by One:
    Best Case    : O(n)
    Average Case : O(n)
    Worst Case   : O(n)

- Rotate by n:
    Best Case    : O(n)
    Average Case : O(n)
    Worst Case   : O(n)

Space Complexity:
- O(n)
  (NumPy slicing and concatenation create new arrays.)

Key Learning:
- Left rotation is the opposite of right rotation.
- The Reversal Algorithm rotates the array in linear time.
- Always use `n % len(arr)` to handle rotations larger than the
  array size.
---------------------------------------------------------
"""

from numpy import array, concatenate


def left_rotation_generic(arr, n):
    """
    Rotate the array to the left by n positions.
    """

    # Handle cases where n is greater than array length
    n = n % len(arr)

    # Reverse the first n elements
    arr = concatenate((arr[:n][::-1], arr[n:]))

    # Reverse the remaining elements
    arr = concatenate((arr[:n], arr[n:][::-1]))

    # Reverse the complete array
    return arr[::-1]


# Driver Code
arr = array([2, 4, 6, 8])

print("Left Rotation by 3:", left_rotation_generic(arr, 3))
