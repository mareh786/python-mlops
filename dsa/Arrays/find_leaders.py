"""
---------------------------------------------------------
Program: Find Leaders in an Array

Approach:
- Traverse each element of the array.
- For every element, check all the elements to its right.
- If no element on the right is greater than the current element,
  then the current element is a leader.
- Store all leader elements in a result list.
- Return the list of leaders.

Time Complexity:
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
  (For every element, the remaining elements may need to be checked.)

Space Complexity:
- O(k), where k is the number of leaders.
  (In the worst case, O(n) if every element is a leader.)

Key Learning:
- A leader is an element that is greater than or equal to all
  the elements to its right.
- This is the brute-force approach.
- An optimized solution exists using reverse traversal with
  O(n) time complexity.
---------------------------------------------------------
"""

from numpy import array


def find_leaders(arr):
    # List to store leader elements
    result = []

    # Traverse the array
    for i in range(len(arr)):
        # Assume the current element is a leader
        is_leader = True

        # Check all elements to the right
        for j in range(i + 1, len(arr)):
            # If a greater element is found,
            # current element is not a leader
            if arr[j] > arr[i]:
                is_leader = False
                break

        # Add the element if it is a leader
        if is_leader:
            result.append(arr[i])

    return result


# Driver Code
arr = array([9, 10, 8, 9, 7, 5])

print("Leaders in the array:", find_leaders(arr))
