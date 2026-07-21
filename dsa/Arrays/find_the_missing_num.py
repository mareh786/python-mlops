"""
---------------------------------------------------------
Program: Find the Missing Number in an Array
(Exactly One Number is Missing)

Approach:
- The array contains numbers from 1 to n with exactly one
  missing number.
- Calculate the expected sum of numbers from 1 to n using
  the formula:
      n * (n + 1) // 2
- Calculate the actual sum of the given array.
- The difference between the expected sum and actual sum
  gives the missing number.
- Return the missing number.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed once while calculating the sum.)

Space Complexity:
- O(1)
  (Only a few extra variables are used.)

Key Learning:
- The mathematical formula eliminates the need for nested loops.
- This is one of the most common interview questions on arrays.
- The approach assumes exactly one number is missing and that
  the numbers range from 1 to n.
---------------------------------------------------------
"""

from numpy import array


def find_missing_number(arr):
    # Total numbers should be n
    n = len(arr) + 1

    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2

    # Calculate the actual sum of the array
    actual_sum = sum(arr)

    # The difference is the missing number
    missing_number = expected_sum - actual_sum

    return missing_number


# Driver Code
arr = array([1, 2, 3, 5])

print("Missing Number:", find_missing_number(arr))
