
"""
---------------------------------------------------------
Program: Linear Search in an Array

Approach:
- Traverse the array from left to right.
- Compare each element with the target value.
- If the target element is found, return its index.
- If the complete array is traversed and the element is not found,
  return -1.

Time Complexity:
- Best Case: O(1)
  (Target element is present at the first index.)

- Average Case: O(n)
  (Target element is present somewhere in the middle.)

- Worst Case: O(n)
  (Target element is at the last index or not present.)

Space Complexity:
- O(1)
  (No extra space is used apart from variables.)

Key Learning:
- Linear Search works on both sorted and unsorted arrays.
- It checks elements sequentially.
- It is useful for small datasets.
---------------------------------------------------------
"""

from numpy import array


def search(arr, target):
    # Traverse the array from index 0 to last index
    for i in range(len(arr)):

        # Check if current element matches the target
        if arr[i] == target:
            return i  # Return index if target is found

    # Return -1 if target element does not exist in array
    return -1


# Driver Code
val = array([1, 3, 5, 7])

print("Element found at index:", search(val, 5))
