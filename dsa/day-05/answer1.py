# list = [9, 7, 12, 97, 89]
# largest = list[0]
# print(largest)
# for i in list:
#     if largest < i:
#         largest = i
# list.remove(largest)
# print(list)        
# print(largest)

# second_largest = list[0]
# for i in list:
#     if second_largest < i:
#         second_largest = i
# print(second_largest)


def main_function(nums):
    l1 = -99999
    l2 = -99999
    
    for i in nums:
        if i > l1:
            l2 = l1
            l1 = i
        elif l2 < i and l2 < l1:
            l2 = i
    return l1, l2
a, b= main_function([-4] )
if b == -99999:
    b = "No second largest number exists"
print(a,b)