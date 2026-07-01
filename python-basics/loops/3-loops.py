# A list of characters
l1 = ["a", "b", "c", "d"]

# Loop through each element in l1
for x in l1:
    # x will take values one by one: a, b, c, d
    print(f"The items are {x}")


# enumerate() adds an index (starting from 10 here)
# IMPORTANT: use a different variable name instead of l1 to avoid overwriting the list
for id, item in enumerate(l1, start=10):
    # id = 10,11,12,13
    # item = a,b,c,d
    print(f"{id}: {item}")


# New lists for pairing
l3 = ["a", "b", "c", "d"]
l2 = ["1", "2", "3", "4"]

# zip() combines two lists element by element
for a, b in zip(l2, l3):
    # a comes from l2 → 1,2,3,4
    # b comes from l3 → a,b,c,d
    print(f"{a} is {b}")