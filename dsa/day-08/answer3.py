# Find the intersection of two lists
# Approach 1
def intersect(lst1, lst2):
 intersection= list(set(lst1) & set(lst2))
 return intersection

print(intersect([1,2,3,4,5], [3,4,5,6,7]))

# Approach 2
def inter(lst1, lst2):
    final = []
    for ch in lst1:
        if ch in lst2:
            final.append(ch)
    return final

print(inter(["a","b","c"], ["c", "d", "a"]))
