# Check if a list contains consecutive integers, regardless of their order

def consecutive_check(nums):
    # Sort the list in ascending order
    sorted_nums = sorted(nums)

    # Check if the difference between consecutive elements is 1
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] != 1:
            return False

    # If all adjacent elements differ by 1, the list is consecutive
    return True


# Example usage
print(consecutive_check([8, 9, 7, 6]))
