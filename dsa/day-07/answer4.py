# Problem 4: Check if two lists contain same Elements
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