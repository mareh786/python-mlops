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


# def main_function(nums):
#     l1 = -99999
#     l2 = -99999
    
#     for i in nums:
#         if i > l1:
#             l2 = l1
#             l1 = i
#         elif l2 < i < l1:
#             l2 = i
#     return l1, l2
# a, b= main_function([-4] )
# if b == -99999:
#     b = "No second largest number exists"
# print(a,b)

def second_largest(nums):
    if len(nums) < 2:
        return "Need at least two numbers"

    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num

        elif second < num < largest:
            second = num

    if second == float('-inf'):
        return "No second largest number exists"

    return second


print(second_largest([10, 5, 8, 20, 15]))  # 15
print(second_largest([-4]))                # Need at least two numbers
print(second_largest([5, 5, 5]))          # No second largest number exists