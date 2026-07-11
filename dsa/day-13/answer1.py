# Function to find the largest, second largest, and third largest
# distinct numbers in a list.

def thr_lrgst_num(nums):
    # Initialize largest, second, and third with negative infinity
    largest = second = third = float('-inf')

    # Traverse through each number in the list
    for num in nums:

        # If the current number is greater than the largest
        if num > largest:
            third = second
            second = largest
            largest = num

        # If the current number is between largest and second largest
        elif largest > num > second:
            third = second
            second = num

        # If the current number is between second and third largest
        elif second > num > third:
            third = num

    # Return the three largest distinct numbers
    return largest, second, third


# Example
print(thr_lrgst_num([10, 10, 20, 5]))
