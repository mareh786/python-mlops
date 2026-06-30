def func(list):
    isSorted= False
    list1= sorted(list)
    if list == list1:
        isSorted = True   
    return isSorted

value = func(["1", "7", "9"])

if value == True:
    print("The list is sorted")
else:
    print("The list in not sorted")