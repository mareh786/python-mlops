# Count even and odd numbers

def counting_even_and_odd(lst):
    even_lst = [num for num in lst if num % 2 == 0]
    odd_lst = [num for num in lst if num % 2 == 1]
    return len(even_lst), len(odd_lst)

v1, v2 = counting_even_and_odd([1, 2, 3, 4, 5, 6, 8])

print(f"Number of evens: {v1}")
print(f"Number of odds: {v2}")
