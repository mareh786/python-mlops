
"""
---------------------------------------------------------
Program: Rearrange Array by Sign
(+ve, -ve, +ve, -ve, ...)

Approach:
- Create two separate lists:
    - One for positive numbers.
    - One for negative numbers.
- Traverse the array once and place each element into its
  respective list.
- Traverse both lists simultaneously.
- Alternately append one positive and one negative element
  to the final array.
- Return the rearranged array.

Assumption:
- The number of positive and negative elements is equal.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (The array is traversed twice.)

Space Complexity:
- O(n)
  (Additional lists are used to store positive, negative,
  and final elements.)

Key Learning:
- Partitioning elements based on a condition is a common DSA
  technique.
- This problem is frequently solved using extra space.
- If unequal numbers of positives and negatives are allowed,
  additional handling is required.
---------------------------------------------------------
"""

import numpy as np


def rearrange_array(arr):
    # List to store positive numbers
    positive = []

    # List to store negative numbers
    negative = []

    # Final rearranged array
    result = []

    # Separate positive and negative numbers
    for num in arr:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)

    # Alternate positive and negative elements
    for i in range(len(positive)):
        result.append(positive[i])
        result.append(negative[i])

    return result


# Driver Code
arr = np.array([1, 2, 3, -1, -2, -3])

print("Rearranged Array:", rearrange_array(arr))
