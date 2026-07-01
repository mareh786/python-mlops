list1 =["a", "b", "c", "d", "e"]

print(f"The list contents are: {list1}")

list1.append("f")

print(f"The list contents are: {list1}")

list2 =["A", "B", "C"]

print(f"The list contents are: {list2}")

list2.extend(list1)

print(f"The list contents are: {list2}")

list2.reverse()

print(f"The list contents are: {list2}")

list2.sort()

print(f"The list contents are: {list2}")
