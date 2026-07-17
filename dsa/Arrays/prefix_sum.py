"""
---------------------------------------------------------
Program: Compute the Prefix Sum of an Array

Approach:
- Initialize a variable `running_sum` to 0.
- Create an empty list `prefix_sum_array`.
- Traverse the array from left to right.
- Add the current element to `running_sum`.
- Append `running_sum` to the prefix sum array.
- Return the prefix sum array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(n)
  (A new array is created to store the prefix sums.)

Key Learning:
- Prefix Sum stores the cumulative sum of elements.
- It helps answer range sum queries efficiently.
- Widely used in competitive programming and DSA problems.
---------------------------------------------------------
"""

from numpy import array


def prefix_sum(arr):
    # Initialize the running sum
    running_sum = 0

    # List to store prefix sums
    prefix_sum_array = []

    # Traverse the array
    for num in arr:

        # Update the running sum
        running_sum += num

        # Store the current prefix sum
        prefix_sum_array.append(running_sum)

    # Return the prefix sum array
    return prefix_sum_array


# Driver Code
arr = array([1, 2, 3, 4, 5, 6])

print("Prefix Sum Array:", prefix_sum(arr))
