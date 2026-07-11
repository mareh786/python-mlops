# Separate even and odd numbers while keeping their original order

def separation(nums):
    # Store all even numbers in their original sequence
    evens = [num for num in nums if num % 2 == 0]

    # Store all odd numbers in their original sequence
    odds = [num for num in nums if num % 2 == 1]

    # Combine evens first, followed by odds
    new_list = evens + odds

    # Return the rearranged list
    return new_list


# Test the function
print(separation([1, 2, 3, 4, 5, 6, 7, 8]))
