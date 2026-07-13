"""
---------------------------------------------------------
Program: Reverse an Array (Without Using Slicing or reverse())

Approach:
- Use the Two-Pointer Technique.
- Initialize one pointer at the beginning (i) and another
  at the end (j) of the array.
- Swap the elements at both pointers.
- Move the left pointer forward and the right pointer
  backward until they meet or cross.
- Return the reversed array.

Time Complexity:
- O(n), where n is the number of elements in the array.
  (Each element is swapped at most once.)

Space Complexity:
- O(1)
  (The reversal is performed in-place without using
  any extra array.)
---------------------------------------------------------
"""

from numpy import array


def reverse_array(arr):
    # Initialize two pointers
    i = 0
    j = len(arr) - 1

    # Swap elements until the pointers meet
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]

        # Move pointers
        i += 1
        j -= 1

    # Return the reversed array
    return arr


# Driver code
arr = array([1, 2, 3, 4])
print("Reversed array:", reverse_array(arr))
