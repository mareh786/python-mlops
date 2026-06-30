# Write a function that returns the index of a target element in a list.
def func(list, target):
    return list.index(target)

print(func(["a", "b", "c"], "c"))

def find_index(list, target):
    if target in list:
        return f"{target} is located at {list.index(target)}th index"
    else: 
        return f"{target} not found in the list"

    
print(find_index(["a", "b", "c"], "a"))