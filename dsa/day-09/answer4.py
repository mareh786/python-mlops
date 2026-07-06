# Find the second smallest number in a list

def second_smallest(lst):
    if len(lst) < 2:
        return None

    unique = list(set(lst))
    unique.sort()

    if len(unique) < 2:
        return None

    return unique[1]

value = second_smallest([5, 4, 3, 4, 1, 7, -1, -2])

print(f"The second smallest number is {value}")
