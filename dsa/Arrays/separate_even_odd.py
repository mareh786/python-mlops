"""
---------------------------------------------------------
Program: Separate Even and Odd Numbers in an Array

Approach:
- Create two separate lists:
    - `even` to store all even numbers.
    - `odd` to store all odd numbers.
- Traverse the array once.
- If an element is even, append it to the `even` list.
- Otherwise, append it to the `odd` list.
- Concatenate the `even` and `odd` lists.
- Return the resulting array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(n)
  (Two additional lists are used to store the even and odd elements.)

Key Learning:
- Partition an array based on a condition.
- Preserves the relative order of even and odd elements.
- Simple and easy-to-understand approach.
- An in-place solution using the two-pointer technique is also possible.
---------------------------------------------------------
"""

from numpy import array


def separate_even_odd(arr):
    # List to store even numbers
    even = []

    # List to store odd numbers
    odd = []

    # Traverse the array
    for num in arr:

        # Check if the number is even
        if num % 2 == 0:
            even.append(num)

        # Otherwise, it is odd
        else:
            odd.append(num)

    # Combine even numbers followed by odd numbers
    result = even + odd

    return result


# Driver Code
arr = array([9, 7, 8, 5, 12])

print("Separated Array:", separate_even_odd(arr))
