"""
---------------------------------------------------------
Program: Rotate an Array to the Right

Approach 1: Rotate Right by One Position
- Reverse the first (n-1) elements.
- Keep the last element unchanged.
- Reverse the entire array.
- The last element moves to the first position.

Approach 2: Rotate Right by k Positions (Reversal Algorithm)
- Find the partition index: k = len(arr) - n.
- Reverse the first part.
- Reverse the second part.
- Reverse the entire array.
- This rotates the array to the right by n positions.

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
- The Reversal Algorithm is one of the most popular ways to rotate
  an array efficiently.
- For NumPy arrays, slicing and concatenation are convenient.
- In interviews, an in-place reversal algorithm is often preferred,
  which achieves O(1) extra space.
---------------------------------------------------------
"""

from numpy import array, concatenate


def rotate_array_right(arr):
    """
    Rotate the array to the right by one position.
    """

    # Reverse the first (n-1) elements and keep the last element unchanged
    rotated = concatenate((arr[:-1][::-1], arr[-1:]))

    # Reverse the complete array
    return rotated[::-1]


# Driver Code
arr = array([1, 2, 3, 4])

print("Rotate Right by One:", rotate_array_right(arr))


# -----------------------------------------------------


def rotate_array_by_n_right(arr, n):
    """
    Rotate the array to the right by n positions.
    """

    # Handle cases where n is greater than array length
    n = n % len(arr)

    # Find partition index
    k = len(arr) - n

    # Reverse the first part
    arr = concatenate((arr[:k][::-1], arr[k:]))

    # Reverse the second part
    arr = concatenate((arr[:k], arr[k:][::-1]))

    # Reverse the complete array
    return arr[::-1]


# Driver Code
arr1 = array([2, 4, 6, 8, 10])

print("Rotate Right by 3:", rotate_array_by_n_right(arr1, 3))
