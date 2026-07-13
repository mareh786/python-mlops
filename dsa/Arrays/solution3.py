"""
---------------------------------------------------------
Program: Check if an Array is Sorted

Approach:
- Traverse the array from the first element to the second-last element.
- Compare each element with its next element.
- If any element is greater than the next element, the array is
  not sorted in ascending order.
- Otherwise, the array is sorted.

Time Complexity:
- O(n), where n is the number of elements in the array.
  (Each element is compared once.)

Space Complexity:
- O(1)
  (Only one extra boolean variable is used.)
---------------------------------------------------------
"""

from numpy import array


def is_sorted(arr):
    # Assume the array is sorted
    sorted_flag = True

    # Compare adjacent elements
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            sorted_flag = False
            break  # No need to check further

    return sorted_flag


# Driver code
val = array([9, 1, 2, 4, 5])
print("Is the array sorted?", is_sorted(val))
