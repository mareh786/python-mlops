"""
---------------------------------------------------------
Program: Merge Two Sorted Arrays

Approach:
- Initialize two pointers:
    - `i` for the first array.
    - `j` for the second array.
- Compare the current elements of both arrays.
- Append the smaller element to the result array.
- Move the corresponding pointer forward.
- Once one array is exhausted, append the remaining elements
  from the other array.
- Return the merged sorted array.

Time Complexity:
- Best Case: O(n + m)
- Average Case: O(n + m)
- Worst Case: O(n + m)
  (Every element from both arrays is visited exactly once.)

Space Complexity:
- O(n + m)
  (A new array is created to store the merged result.)

Key Learning:
- The Two Pointer Technique efficiently merges two sorted arrays.
- This technique is used in the Merge Sort algorithm.
- Since both arrays are already sorted, no additional sorting is needed.
---------------------------------------------------------
"""

from numpy import array


def merge_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    i = 0
    j = 0

    # List to store merged elements
    result = []

    # Compare elements until one array is exhausted
    while i < len(arr1) and j < len(arr2):

        # Append the smaller element
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append remaining elements from the first array
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Append remaining elements from the second array
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# Driver Code
arr1 = array([1, 3, 5])
arr2 = array([2, 4, 6])

print("Merged Sorted Array:", merge_sorted_arrays(arr1, arr2))
