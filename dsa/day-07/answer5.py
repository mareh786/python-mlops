# Problem 5: FLoyd's Triangle
num = 1
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num+=1
    print()

def floyd_triangle(first_num, rows):
    for i in range(i, rows+1):
        for j in range(1, i+1):
            print(first_num, end= " ")
            first_num+=1
        print()
floyd_triangle(10, 5)