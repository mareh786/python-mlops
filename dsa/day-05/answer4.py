# Problem 4: Find All Numbers Divisible by 3

def func(x):
    y = []
    for i in x:
        if i%3==0 :
            y.append(i)
    return y
value = func([1, 10])
if not value:
    print("None of the numbers are divisible by 3")
else:
    print(value)