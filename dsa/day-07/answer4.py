# Problem 4: Check if two lists contain same Elements
# Approach 1
list1= [1,2,3,4,5]
list2= [4,5,6,7,8]
common = []
count = 0
for i in list1:
    for j in list2:
        if i==j:
            common.append(i)
            count+=1
print(f"There are {count} common elements and those are {common}")

# Approach 2

intersect= list(set(list1) & set(list2))
print(intersect)

# Approach 3

def common_element(lst1, lst2):
    result =[]
    number= 0
    for i in lst1:
        for j in lst2:
            if i==j:
                result.append(i)
                number+=1
    interset= list(set(lst1) & set(lst2))
    return number, result, interset
    

num, res, inter= common_element(["a","b", "c", "d"], ["c", "d", "e", "f"])
print(f"There are {num} common elements and those are {res}")