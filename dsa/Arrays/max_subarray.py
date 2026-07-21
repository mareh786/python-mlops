
"""
---------------------------------------------------------
Program: Maximum Sum Subarray (Kadane's Algorithm)

Approach:
- Initialize:
    - `current_sum` to store the sum of the current subarray.
    - `max_sum` to store the maximum subarray sum found so far.
- Traverse the array from left to right.
- Add the current element to `current_sum`.
- Update `max_sum` if `current_sum` is greater.
- If `current_sum` becomes negative, reset it to 0 because a
  negative sum cannot contribute to a maximum sum subarray.
- Return `max_sum`.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(1)
  (Only two extra variables are used.)

Key Learning:
- Kadane's Algorithm is the optimal solution for the Maximum
  Subarray Sum problem.
- A negative running sum is discarded because it decreases the
  sum of any future subarray.
- This is one of the most frequently asked interview questions.
---------------------------------------------------------
"""

import numpy as np


def max_subarray(arr):
    # Initialize current and maximum sum
    current_sum = 0
    max_sum = arr[0]

    # Traverse the array
    for num in arr:

        # Add current element to running sum
        current_sum += num

        # Update maximum sum if needed
        max_sum = max(current_sum, max_sum)

        # Reset running sum if it becomes negative
        if current_sum < 0:
            current_sum = 0

    # Return the maximum subarray sum
    return max_sum


# Driver Code
arr = np.array([2, 3, -5, 6, -4])

print("Maximum Subarray Sum:", max_subarray(arr))
