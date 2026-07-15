"""
---------------------------------------------------------
Program: Count Even and Odd Numbers in an Array

Approach:
- Initialize two counters: `even` and `odd` to 0.
- Traverse the array from left to right.
- Check each element:
    - If the element is divisible by 2, increment the even counter.
    - Otherwise, increment the odd counter.
- Return the total count of even and odd numbers.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)
  (Each element is visited exactly once.)

Space Complexity:
- O(1)
  (Only two extra variables are used to store the counts.)

Key Learning:
- Use the modulo (%) operator to determine whether a number is even or odd.
- Traverse the array only once for an efficient solution.
- Multiple values can be returned from a function using tuples.
---------------------------------------------------------
"""

from numpy import array


def count_even_odd(arr):
    # Initialize counters
    even = 0
    odd = 0

    # Traverse the array
    for num in arr:

        # Check if the number is even
        if num % 2 == 0:
            even += 1

        # Otherwise, it is odd
        else:
            odd += 1

    # Return the count of even and odd numbers
    return even, odd


# Driver Code
arr = array([12, 5, 8, 9])

even_count, odd_count = count_even_odd(arr)

print("Even Count:", even_count)
print("Odd Count:", odd_count)
