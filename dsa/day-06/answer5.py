# Problem 5: Find all Factors of the number
def factorisation(num):
    factor = []
    for n in range(1, num+1):
        if num%n == 0:
            factor.append(n)

print(factorisation(24))