# a = 1987654321
# print(type(a))
# sum = 0
# while a > 0:
#     digit = a%10
#     sum += digit
#     a //=10
    
# print(sum)
# a = 12345
# while a > 0 :
#     print(a // 10)
#     a //= 10



def sumofdig():
    a = int(input("Enter The Number: "))
    sum = 0
    while a > 0:
        digit = a%10
        sum += digit
        a //= 10
    return sum

print(sumofdig())