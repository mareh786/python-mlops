"""
---------------------------------------------------------
Program: Find the First Occurrence of an Element in an Array

Approach:
- Traverse the array from left to right.
- Compare each element with the target value.
- As soon as the target is found, return its index.
- If the entire array is traversed and the target is not found,
  return -1.

Time Complexity:
- Best Case: O(1)
  (Target is present at the first index.)

- Average Case: O(n)
  (Target is present somewhere in the middle.)

- Worst Case: O(n)
  (Target is at the last index or not present.)

Space Complexity:
- O(1)
  (No extra space is used.)

Key Learning:
- Linear search returns the first occurrence of an element.
- Early termination improves efficiency when the target is found.
- Can be implemented using both Object-Oriented Programming (OOP)
  and Functional Programming approaches.
---------------------------------------------------------
"""

from numpy import array


class FindElement:
    def __init__(self, arr, target):
        # Initialize the array and target element
        self.arr = arr
        self.target = target

    def find_index(self):
        # Traverse the array
        for i in range(len(self.arr)):

            # Check if the current element matches the target
            if self.arr[i] == self.target:
                return i  # Return the first occurrence index

        # Target not found
        return -1


# Driver Code (OOP Approach)
array1 = array([1, 2, 3, 4, 5, 6, 7])

case1 = FindElement(array1, 10)

print("OOP Approach:", case1.find_index())


# Function-Based Approach
def find_index_of_target(arr, target):
    # Traverse the array
    for i in range(len(arr)):

        # Check if the current element matches the target
        if arr[i] == target:
            return i  # Return the first occurrence index

    # Target not found
    return -1


# Driver Code (Function Approach)
arr = array([1, 2, 3, 4, 5, 6])

print("Function Approach:", find_index_of_target(arr, 5))
