"""
---------------------------------------------------------
Program: Count Occurrences of an Element in an Array

Approach:
- Initialize a counter variable to 0.
- Traverse the array from left to right.
- Compare each element with the target value.
- Increment the counter whenever the target is found.
- Return the total count after traversing the entire array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The entire array must be traversed regardless of where the target is.)

Space Complexity:
- O(1)
  (Only one extra variable is used to store the count.)

Key Learning:
- Traversing an array using a loop.
- Counting occurrences using a counter variable.
- Useful when duplicate elements may exist.
---------------------------------------------------------
"""

from numpy import array


def count_occurrence(arr, target):
    # Initialize count to zero
    count = 0

    # Traverse each element in the array
    for element in arr:

        # Increment count if target is found
        if element == target:
            count += 1

    # Return the total count
    return count


# Driver Code
arr = array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

count = count_occurrence(arr, 5)

# Check if the target exists in the array
if count != 0:
    print(f"Element occurs {count} time(s).")
else:
    print("The element is not present in the array.")
