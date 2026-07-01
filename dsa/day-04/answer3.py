# #Return a new list containing only the first occurrence of each element.

# def unique(list):
#     uniq = {x for x in list}
#     return uniq

# print(unique(["a", "b", "c", "a", "c"]))

def unique(list):
    fresh= []
    for x in list:
        if x not in fresh:
            fresh.append(x)
    return fresh

print(unique(["a", "b", "c", "a", "c"]))
print(unique([1, 2, 2, 3, 1, 4]))