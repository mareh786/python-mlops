def func(list1):
    minimum = list1[0]

    for item in list1:
        if item < minimum:
            minimum = item

    return minimum


print(func([12, 13, 15, 18]))