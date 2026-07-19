"""
---------------------------------------------------------
Program: Check if One Array is a Rotation of Another

Approach:
- If the lengths of both arrays are different, they cannot be
  rotations of each other.
- Concatenate the first array with itself.
- If the second array appears as a contiguous subarray in the
  concatenated array, then it is a rotation.
- Otherwise, it is not a rotation.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)
  (Each slice comparison can take O(n), and there are O(n) slices.)

Space Complexity:
- O(n)
  (A new concatenated array of size 2n is created.)

Key Learning:
- A rotation of an array always appears as a subarray in the
  original array concatenated with itself.
- This is a commonly used trick in array and string problems.
---------------------------------------------------------
"""

from numpy import array, concatenate


def is_rotation(arr1, arr2):
    # Arrays with different lengths cannot be rotations
    if len(arr1) != len(arr2):
        return False

    # Concatenate the first array with itself
    doubled_array = concatenate((arr1, arr1))

    # Length of the second array
    n = len(arr2)

    # Check every possible subarray of length n
    for i in range(len(doubled_array) - n + 1):

        # If a matching subarray is found,
        # arr2 is a rotation of arr1
        if all(doubled_array[i:i + n] == arr2):
            return True

    # No matching subarray found
    return False


# Driver Code
arr1 = array([1, 2, 3, 4])
arr2 = array([4, 3, 1, 2])

print("Is Rotation:", is_rotation(arr1, arr2))
