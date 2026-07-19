"""
---------------------------------------------------------
Program: Check if an Array is a Palindrome

Approach:
- Initialize two pointers:
    - `left` at the beginning of the array.
    - `right` at the end of the array.
- Compare the elements at both pointers.
- If they are not equal, the array is not a palindrome.
- Move `left` one step to the right and `right` one step to the left.
- Continue until both pointers meet or cross each other.
- If all corresponding elements are equal, the array is a palindrome.

Time Complexity:
- Best Case: O(1)
  (First comparison itself is unequal.)

- Average Case: O(n)

- Worst Case: O(n)
  (All elements must be checked.)

Space Complexity:
- O(1)
  (Only two pointer variables are used.)

Key Learning:
- The Two Pointer Technique is an efficient way to check for a palindrome.
- Compare elements from both ends simultaneously.
- No extra array or string conversion is required.
---------------------------------------------------------
"""

from numpy import array


def check_palindrome(arr):
    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Compare elements from both ends
    while left < right:

        # If elements are different, it is not a palindrome
        if arr[left] != arr[right]:
            return False

        # Move both pointers
        left += 1
        right -= 1

    # All corresponding elements matched
    return True


# Driver Code
arr = array([1, 2, 3, 3, 9, 2, 1])

print("Is Palindrome:", check_palindrome(arr))
