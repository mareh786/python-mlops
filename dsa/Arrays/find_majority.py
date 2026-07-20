"""
---------------------------------------------------------
Program: Find the Majority Element in an Array
(Boyer-Moore Voting Algorithm)

Approach:
- Traverse the array to find a potential majority candidate.
- Maintain a candidate and its count.
- If the count becomes zero, choose the current element as the
  new candidate.
- Increase the count if the current element matches the candidate;
  otherwise, decrease the count.
- After the first pass, verify whether the candidate actually
  appears more than n/2 times.
- Return the candidate if it is a majority element; otherwise,
  return "No majority element found".

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed twice.)

Space Complexity:
- O(1)
  (Only a few extra variables are used.)

Key Learning:
- Boyer-Moore Voting Algorithm finds the majority candidate in
  linear time using constant extra space.
- A second pass is necessary to verify the candidate because
  the first pass only guarantees a potential majority element.
---------------------------------------------------------
"""

from numpy import array


def check_majority(arr):
    # Initialize candidate and count
    candidate = None
    count = 0

    # -------------------------
    # Pass 1: Find a candidate
    # -------------------------
    for num in arr:

        # Select a new candidate when count becomes zero
        if count == 0:
            candidate = num
            count = 1

        # Increase count if the same candidate appears
        elif num == candidate:
            count += 1

        # Otherwise decrease the count
        else:
            count -= 1

    # ----------------------------
    # Pass 2: Verify the candidate
    # ----------------------------
    actual_count = 0

    for num in arr:
        if num == candidate:
            actual_count += 1

    # Check if the candidate occurs more than n/2 times
    if actual_count > len(arr) // 2:
        return candidate

    return "No majority element found"


# Driver Code
arr = array([1, 2, 3, 3, 9, 2, 1, 3, 3, 3, 3, 3])

print("Majority Element:", check_majority(arr))
