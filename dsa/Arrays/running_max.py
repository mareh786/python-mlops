"""
---------------------------------------------------------
Program: Find the Running Maximum in an Array

Approach:
- Assume the first element is the current maximum (`running_max`).
- Create an empty list to store the running maximum values.
- Traverse the array from left to right.
- If the current element is greater than the current maximum,
  update the running maximum.
- Append the current running maximum to the result list.
- Return the result list.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(n)
  (A new array is used to store the running maximum values.)

Key Learning:
- Running Maximum keeps track of the largest element seen so far.
- It is useful in many DSA problems involving prefixes.
- Similar to Prefix Sum, but instead of storing cumulative sums,
  it stores cumulative maximum values.
---------------------------------------------------------
"""

from numpy import array


def find_running_max(arr):
    # Assume the first element is the running maximum
    running_max = arr[0]

    # List to store running maximum values
    result = []

    # Traverse the array
    for num in arr:

        # Update the running maximum if a larger element is found
        if num > running_max:
            running_max = num

        # Store the current running maximum
        result.append(running_max)

    # Return the running maximum array
    return result


# Driver Code
arr = array([3, 1, 5, 2, 6])

print("Running Maximum Array:", find_running_max(arr))
