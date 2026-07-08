# Difference Between Minimum and Maximum Number in a List

# Approach 1: Using sorting
# def diff(lst):
#     # Sort the list in ascending order
#     lst.sort()
#
#     # Calculate the difference between the largest and smallest elements
#     difference = lst[len(lst) - 1] - lst[0]
#
#     # Return the result
#     return difference
#
# print(diff([9, 6, 4, 7, 8]))


# Approach 2: Finding minimum and maximum manually
def approach2(nums):
    # Initialize minimum and maximum with the first element
    minimum = nums[0]
    maximum = nums[0]

    # Traverse the list to find the minimum and maximum values
    for num in nums:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    # Return the difference between maximum and minimum
    return maximum - minimum


# Call the function and print the result
print(f"The difference between the minimum and maximum numbers is {approach2([9, 4, 3, 6])}")
