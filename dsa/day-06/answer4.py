# Problem 4: Finding common elements in two lists

def commonChar(lst1, lst2):
    commonPresent = False
    for char in lst1:
        if char in lst2:
            commonPresent = True
    return commonPresent

value = commonChar([1, 2, 3, 4], [1, 9, 7, 5])

if value == True:
    print("Common element exists")
else: 
    print("No common elements")
