# Check if a Number is Prime

def prime(num):
    isPrime = True
    if num <= 1:
        isPrime= False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0: 
                isPrime = False
    return isPrime

number= int(input("Enter a number to check:"))
value = prime(number)
if value == True:
    print(f"{number} is a prime number!!!")
    
else:
    print(f"{number} is composite number!")