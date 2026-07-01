# Loop from 1 to 10 (11 is excluded, so range is 1–10)
for number in range(1, 11):

    # Multiply the current number with 5 and print result
    # number → 1,2,3,...10
    # number * 5 → 5,10,15,...50

    # f-string is used to format the output nicely
    print(f"5 X {number} = {number * 5}")