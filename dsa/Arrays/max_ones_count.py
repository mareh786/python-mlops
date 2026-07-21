"""
---------------------------------------------------------
Program: Count the Maximum Number of Consecutive Ones

Approach:
- Initialize two variables:
    - `count` to keep track of the current consecutive ones.
    - `max_count` to store the maximum consecutive ones found.
- Traverse the array from left to right.
- If the current element is 1:
    - Increment `count`.
    - Update `max_count` if `count` is greater.
- Otherwise:
    - Reset `count` to 0.
- After traversing the array, return the maximum count.
- If no 1s are present, return an appropriate message.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(1)
  (Only two extra variables are used.)

Key Learning:
- Maintain a running count while traversing the array.
- Reset the count whenever a non-one element is encountered.
- This is a classic sliding count problem.
---------------------------------------------------------
"""

from numpy import array


def count_max_consecutive_ones(arr):
    # Initialize counters
    count = 0
    max_count = 0

    # Traverse the array
    for num in arr:

        # Check if the current element is 1
        if num == 1:
            count += 1

            # Update maximum count
            if count > max_count:
                max_count = count

        # Reset count when a non-one is encountered
        else:
            count = 0

    # Check if the array contains any 1s
    if max_count == 0:
        return "No ones in the array"

    return max_count


# Driver Code
arr = array([0, 0, 0, 0, 0])

print("Maximum Consecutive Ones:", count_max_consecutive_ones(arr))
