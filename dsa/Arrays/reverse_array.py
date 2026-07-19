
"""
---------------------------------------------------------
Program: Reverse an Array In-Place

Approach:
- Initialize two pointers:
    - `left` at the beginning of the array.
    - `right` at the end of the array.
- Swap the elements at `left` and `right`.
- Move `left` one step to the right.
- Move `right` one step to the left.
- Continue until both pointers meet or cross each other.
- Return the reversed array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is swapped at most once.)

Space Complexity:
- O(1)
  (The array is reversed in-place without using extra space.)

Key Learning:
- The Two Pointer Technique is an efficient way to reverse an array.
- Swapping elements from both ends eliminates the need for an extra array.
- This is one of the most common interview questions on arrays.
---------------------------------------------------------
"""

from numpy import array


def reverse_array(arr):
    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Swap elements until the pointers meet
    while left < right:

        # Swap the left and right elements
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers
        left += 1
        right -= 1

    # Return the reversed array
    return arr


# Driver Code
arr = array([1, 2, 3, 4])

print("Reversed Array:", reverse_array(arr))
