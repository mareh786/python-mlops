# Move all Zeros to the end
# Approach: Create zeros and non-zero lists, and then combine them.
def moving_zeros(lst):
    non_zero = []
    zero = []

    for num in lst:
        if num != 0:
            non_zero.append(num)
        else:
            zero.append(num)

    final_lst = non_zero + zero
    return final_lst

print(moving_zeros([1, 2, 0, 9, 0, 2, 0, 5]))
