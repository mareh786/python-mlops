def sum_of_min_max(lst):
    # Initialize both maximum and minimum with the first element
    maximum = lst[0]
    minimum = lst[0]

    # Traverse the list to find the maximum and minimum values
    for num in lst:
        # Update maximum if a larger value is found
        if num > maximum:
            maximum = num

        # Update minimum if a smaller value is found
        if num < minimum:
            minimum = num

    # Return the sum of the maximum and minimum values
    return maximum + minimum


# Call the function and print the result
print(sum_of_min_max([1, 2, 4, 5, 9]))
