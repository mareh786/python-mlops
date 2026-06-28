list1 = ['1', '2', '3']

list1.append('4')

list1.append('5')

list1.append('6')

print(list1)
evencount=0
for i in range(len(list1)):
    if i%2 == 0:
        evencount +=1
print(evencount)


# Approach 2

def evenCount():
    list2 = []
    list2 = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    print(list2)
    
    count=0
    list3=[]
    for i in range(len(list2)):
        if list2[i]%2==0:
           count+=1 
           list3.append(list2[i])
           
    return count , list3
# evenCount()
count, even_numbers = evenCount()

print(f"There are {count} even numbers and those are {even_numbers}!!")