# Finding the largest odd number

def largest_odd(lst):
    odd = [num for num in lst if num % 2 == 1]

    if len(odd) == 0:
        return "No odd numbers in the list!"

    return max(odd)

print(largest_odd([94, 12, 2, 46, 92]))
