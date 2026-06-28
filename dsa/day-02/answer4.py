def addition():
    list1 = ['1', '12', '3', '14']
    sum = 0
    for each in list1:
        each = int(each)
        if each %2 == 0:
            sum += each
        
    return sum
Sum = addition()

print(f"The sum of even numbers in the list is {Sum}")